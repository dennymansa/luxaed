<?php
/**
 * Moving24 - приёмник заявок (zone.ee, Gmail app-password).
 * Структурированное письмо: Клиент -> Маршрут (Откуда/Куда) -> Детали. Слева.
 * Конверсия: фронту нужен только статус (200 = ушло). Пароль только в config.php.
 */

header('Content-Type: application/json; charset=UTF-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Accept');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST')    { fail(405, 'method'); }

$cfgPath = __DIR__ . '/config.php';
if (!is_file($cfgPath)) { fail(500, 'no-config'); }
$cfg = require $cfgPath;

if (trim((string)($_POST['_gotcha'] ?? '')) !== '') { ok(); }

$values = $_POST;
unset($values['_gotcha'], $values['_subject']);

// сопоставление подписей (любой язык) -> роль
$ROLE_LABELS = [
  'name'       => ['Имя / компания','Nimi / ettevõte','Name / company','Nimi / yritys'],
  'phone'      => ['Телефон','Telefon','Phone','Puhelin'],
  'email'      => ['Email','E-post','Sähköposti'],
  'service'    => ['Услуга','Teenus','Service','Palvelu'],
  'from'       => ['Откуда','Kust','From','Mistä'],
  'from_floor' => ['Этаж (откуда)','Korrus (kust)','Floor (from)','Kerros (mistä)'],
  'from_lift'  => ['Лифт (откуда)','Lift (kust)','Lift (from)','Hissi (mistä)'],
  'to'         => ['Куда','Kuhu','To','Minne'],
  'to_floor'   => ['Этаж (куда)','Korrus (kuhu)','Floor (to)','Kerros (minne)'],
  'to_lift'    => ['Лифт (куда)','Lift (kuhu)','Lift (to)','Hissi (minne)'],
  'date'       => ['Дата','Kuupäev','Date','Päivä'],
  'time'       => ['Время','Kellaaeg','Time','Aika'],
  'packing'    => ['Упаковка от нас','Pakkimine meilt','Packing by us','Pakkaus meiltä'],
  'msg'        => ['Сообщение','Sõnum','Message','Viesti'],
  'page'       => ['Страница','Leht','Page','Sivu'],
];

$V = [];          // роль => значение
$replyTo = '';
$flat = '';
foreach ($values as $label => $val) {
    $clean = str_replace('_', ' ', $label);
    $v = is_array($val) ? implode(', ', $val) : trim((string)$val);
    $flat .= $v;
    if ($replyTo === '' && $v !== '' && filter_var($v, FILTER_VALIDATE_EMAIL)) { $replyTo = $v; }
    foreach ($ROLE_LABELS as $role => $labs) {
        if (in_array($clean, $labs, true)) { $V[$role] = $v; break; }
    }
}
if (trim($flat) === '') { fail(400, 'empty'); }

$photoCount = 0;
foreach ($_FILES as $key => $f) {
    if (strpos($key, 'photo') === 0 && !empty($f['tmp_name']) && (int)$f['error'] === 0) { $photoCount++; }
}

// --- Route map + distance/time (Google Maps; key from config; картинка встраивается inline) ---
$mapCid = ''; $mapPng = ''; $routeInfo = '';
$mapsKey = isset($cfg['maps_key']) ? trim((string)$cfg['maps_key']) : '';
$fromA = trim((string)vv($V,'from')); $toA = trim((string)vv($V,'to'));
if ($mapsKey !== '' && $fromA !== '' && $toA !== '') {
    $poly = '';
    $dj = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/directions/json?units=metric&origin='
        . rawurlencode($fromA) . '&destination=' . rawurlencode($toA) . '&key=' . rawurlencode($mapsKey)), true);
    if (isset($dj['routes'][0])) {
        $poly = isset($dj['routes'][0]['overview_polyline']['points']) ? $dj['routes'][0]['overview_polyline']['points'] : '';
        $leg  = isset($dj['routes'][0]['legs'][0]) ? $dj['routes'][0]['legs'][0] : null;
        if ($leg) {
            $d = isset($leg['distance']['text']) ? $leg['distance']['text'] : '';
            $t = isset($leg['duration']['text']) ? $leg['duration']['text'] : '';
            $routeInfo = trim($d . ($d !== '' && $t !== '' ? '  ·  ~' : '') . $t);
        }
    }
    $murl = 'https://maps.googleapis.com/maps/api/staticmap?size=624x300&scale=2'
        . ($poly !== '' ? '&path=' . rawurlencode('color:0x1d4ed8cc|weight:5|enc:' . $poly) : '')
        . '&markers=' . rawurlencode('color:0x1d4ed8|label:A|' . $fromA)
        . '&markers=' . rawurlencode('color:0x0f9d58|label:B|' . $toA)
        . '&key=' . rawurlencode($mapsKey);
    $png = fetchUrl($murl);
    if ($png !== '' && strncmp($png, "\x89PNG", 4) === 0) { $mapPng = $png; $mapCid = 'routemap'; }
}

// --- Street View зданий по адресам (если есть съёмка) ---
$svFromPng = ''; $svFromCid = ''; $svToPng = ''; $svToCid = '';
if ($mapsKey !== '') {
    if ($fromA !== '') { list($svFromPng, $svFromCid) = streetView($fromA, $mapsKey, 'svfrom'); }
    if ($toA   !== '') { list($svToPng, $svToCid)     = streetView($toA,   $mapsKey, 'svto'); }
}

$subject = trim((string)($_POST['_subject'] ?? '')) ?: 'Заявка с сайта Moving24';

$clientRows = row('Имя / компания', vv($V,'name')) . phoneRow('Телефон', vv($V,'phone')) . mailRow('Email', vv($V,'email'));
$detailRows = row('Услуга', vv($V,'service')) . row('Дата', fmtDate(vv($V,'date'))) . row('Время', vv($V,'time'))
            . row('Упаковка от нас', vv($V,'packing'));
$pageUrl = vv($V,'page');

$html = '<!DOCTYPE html><html><body style="margin:0;background:#eef1f6;padding:24px 20px;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif">'
  . '<table role="presentation" width="640" cellpadding="0" cellspacing="0" align="left" style="max-width:640px;width:100%;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 6px 28px rgba(20,30,50,.12)">'
  . '<tr><td style="background:#1d4ed8;padding:22px 26px">'
  . '<div style="color:#ffffff;font-size:21px;font-weight:800;letter-spacing:.2px">Moving24 - новая заявка</div>'
  . '<div style="color:#bfd2ff;font-size:13px;margin-top:5px">' . esc($subject) . '</div></td></tr>'
  . '<tr><td style="padding:6px 26px 18px">'
  . sectionTitle('Клиент')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%">' . $clientRows . '</table>'
  . sectionTitle('Маршрут')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr>'
  . addrBlock('Откуда', vv($V,'from'), vv($V,'from_floor'), vv($V,'from_lift'), '#1d4ed8', $svFromCid)
  . '<td width="36" align="center" valign="middle" style="color:#c2ccd9;font-size:22px;font-weight:700">&rarr;</td>'
  . addrBlock('Куда', vv($V,'to'), vv($V,'to_floor'), vv($V,'to_lift'), '#0f9d58', $svToCid)
  . '</tr></table>'
  . ($routeInfo !== '' ? '<div style="margin-top:10px;color:#334155;font-size:14px;font-weight:700">&#128662;&nbsp;' . esc($routeInfo) . '</div>' : '')
  . ($mapCid !== '' ? '<div style="margin-top:12px;border-radius:12px;overflow:hidden;border:1px solid #e7ecf3"><img src="cid:' . $mapCid . '" alt="Маршрут" width="624" style="display:block;width:100%;max-width:624px;height:auto"></div>' : '')
  . routeButton(vv($V,'from'), vv($V,'to'))
  . sectionTitle('Детали')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%">' . $detailRows . '</table>'
  . msgBlock(vv($V,'msg'))
  . ($photoCount ? '<div style="margin-top:16px;background:#eef4ff;border:1px solid #d6e4ff;border-radius:10px;padding:12px 16px;color:#1d4ed8;font-size:13px;font-weight:600">&#128206; Фото во вложении: ' . $photoCount . ' шт.</div>' : '')
  . '</td></tr>'
  . '<tr><td style="padding:0 26px 10px"><div style="background:#1d4ed8;border-radius:12px;padding:14px 18px;text-align:center;color:#ffffff;font-size:15px;font-weight:800;letter-spacing:.2px">Красава пацаны, работаем! &#128666;</div></td></tr>'
  . '<tr><td style="padding:8px 26px 20px">'
  . '<div style="color:#9aa4b2;font-size:12px">Страница: ' . ($pageUrl !== '' ? '<a href="' . esc($pageUrl) . '" style="color:#1d4ed8;text-decoration:none">' . esc($pageUrl) . '</a>' : '-') . '</div>'
  . '<div style="color:#cbd5e1;font-size:11px;margin-top:4px">Отправлено формой moving24.ee</div>'
  . '</td></tr></table></body></html>';

$alt = "Заявка Moving24\n\nКЛИЕНТ\n  Имя: " . vv($V,'name') . "\n  Телефон: " . vv($V,'phone') . "\n  Email: " . vv($V,'email')
     . "\n\nМАРШРУТ\n  Откуда: " . vv($V,'from') . " (этаж " . vv($V,'from_floor') . ", лифт " . vv($V,'from_lift') . ")"
     . "\n  Куда: " . vv($V,'to') . " (этаж " . vv($V,'to_floor') . ", лифт " . vv($V,'to_lift') . ")"
     . "\n\nДЕТАЛИ\n  Услуга: " . vv($V,'service') . "\n  Дата: " . fmtDate(vv($V,'date')) . "\n  Время: " . vv($V,'time')
     . "\n  Упаковка: " . vv($V,'packing') . "\n  Сообщение: " . vv($V,'msg')
     . "\n\nФото: " . $photoCount . "\nСтраница: " . $pageUrl;

require __DIR__ . '/phpmailer/src/Exception.php';
require __DIR__ . '/phpmailer/src/PHPMailer.php';
require __DIR__ . '/phpmailer/src/SMTP.php';
$mail = new PHPMailer\PHPMailer\PHPMailer(true);
try {
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = $cfg['gmail_user'];
    $mail->Password = $cfg['gmail_app_password'];
    $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;
    $mail->CharSet = 'UTF-8';

    $mail->setFrom($cfg['gmail_user'], 'moving24.ee - и еще одна');
    $mail->addAddress($cfg['lead_to']);
    if ($replyTo !== '') { $mail->addReplyTo($replyTo); }

    foreach ($_FILES as $key => $f) {
        if (strpos($key, 'photo') !== 0) { continue; }
        if (!empty($f['tmp_name']) && is_uploaded_file($f['tmp_name']) && (int)$f['error'] === 0) {
            $mail->addAttachment($f['tmp_name'], $f['name'] ?: ($key . '.jpg'));
        }
    }

    $embeds = [
        [$mapPng,    $mapCid,    'route.png', 'image/png'],
        [$svFromPng, $svFromCid, 'from.jpg',  'image/jpeg'],
        [$svToPng,   $svToCid,   'to.jpg',    'image/jpeg'],
    ];
    foreach ($embeds as $e) {
        if ($e[1] !== '' && $e[0] !== '') {
            $mail->addStringEmbeddedImage($e[0], $e[1], $e[2], PHPMailer\PHPMailer\PHPMailer::ENCODING_BASE64, $e[3]);
        }
    }

    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body = $html;
    $mail->AltBody = $alt;

    $mail->send();
    ok();
} catch (Throwable $e) {
    error_log('moving24 lead mail failed: ' . $e->getMessage());
    fail(502, 'send');
}

// ---- helpers ----
function vv($V, $k) { return isset($V[$k]) ? $V[$k] : ''; }
function fmtDate($v) {
    $v = trim((string)$v);
    if (preg_match('/^(\d{4})-(\d{2})-(\d{2})$/', $v, $m)) {
        $days = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'];
        $wd = $days[(int)date('w', mktime(0, 0, 0, (int)$m[2], (int)$m[3], (int)$m[1]))];
        return $m[3] . '.' . $m[2] . '.' . $m[1] . ' (' . $wd . ')';
    }
    return $v;
}
function fetchUrl($url) {
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 7, CURLOPT_CONNECTTIMEOUT => 5, CURLOPT_FOLLOWLOCATION => true, CURLOPT_SSL_VERIFYPEER => true]);
        $r = curl_exec($ch); curl_close($ch);
        return $r === false ? '' : (string)$r;
    }
    $ctx = stream_context_create(['http' => ['timeout' => 7], 'https' => ['timeout' => 7]]);
    $r = @file_get_contents($url, false, $ctx);
    return $r === false ? '' : (string)$r;
}
function esc($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }
function sectionTitle($t) {
    return '<div style="color:#94a3b8;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;margin:18px 0 8px">' . esc($t) . '</div>';
}
function row($label, $val) {
    $shown = ($val === '') ? '<span style="color:#aab2bf">-</span>' : nl2br(esc($val));
    return '<tr>'
        . '<td style="padding:6px 0;color:#5b6472;font-size:13px;width:140px;vertical-align:top">' . esc($label) . '</td>'
        . '<td style="padding:6px 0;color:#0f172a;font-size:14px;font-weight:600">' . $shown . '</td></tr>';
}
function phoneRow($label, $val) {
    if ($val === '') { return row($label, ''); }
    $href = preg_replace('/[^0-9+]/', '', $val);
    $link = '<a href="tel:' . esc($href) . '" style="color:#1d4ed8;font-weight:700;font-size:16px;text-decoration:none">&#128222;&nbsp;' . esc($val) . '</a>';
    return '<tr><td style="padding:6px 0;color:#5b6472;font-size:13px;width:140px;vertical-align:top">' . esc($label) . '</td>'
         . '<td style="padding:6px 0">' . $link . '</td></tr>';
}
function mailRow($label, $val) {
    if ($val === '') { return row($label, ''); }
    $link = '<a href="mailto:' . esc($val) . '" style="color:#1d4ed8;font-weight:600;text-decoration:none">' . esc($val) . '</a>';
    return '<tr><td style="padding:6px 0;color:#5b6472;font-size:13px;width:140px;vertical-align:top">' . esc($label) . '</td>'
         . '<td style="padding:6px 0;font-size:14px">' . $link . '</td></tr>';
}
function msgBlock($msg) {
    if (trim((string)$msg) === '') { return ''; }
    return sectionTitle('Сообщение клиента')
        . '<div style="background:#fffbeb;border:1px solid #fde68a;border-left:5px solid #f59e0b;border-radius:12px;padding:16px 18px;color:#1f2937;font-size:16px;line-height:1.55;font-weight:600;white-space:pre-wrap">' . nl2br(esc($msg)) . '</div>';
}
function mapBtn($href, $label, $bg, $fg) {
    return '<a href="' . esc($href) . '" style="display:inline-block;background:' . $bg . ';color:' . $fg . ';font-size:13px;font-weight:700;text-decoration:none;padding:11px 16px;border-radius:10px;margin:0 8px 8px 0">' . $label . '</a>';
}
function routeButton($from, $to) {
    $from = trim((string)$from); $to = trim((string)$to);
    $links = '';
    if ($from !== '' && $to !== '') {
        $g = 'https://www.google.com/maps/dir/?api=1&origin=' . rawurlencode($from) . '&destination=' . rawurlencode($to);
        $links .= mapBtn($g, '&#128506;&nbsp;Маршрут в Google Maps &rarr;', '#1d4ed8', '#ffffff');
    }
    if ($from !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($from) . '&navigate=yes', 'Waze: Откуда', '#33ccff', '#062a3a'); }
    if ($to   !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($to)   . '&navigate=yes', 'Waze: Куда',   '#33ccff', '#062a3a'); }
    return $links === '' ? '' : '<div style="margin-top:12px">' . $links . '</div>';
}
function addrBlock($title, $addr, $floor, $lift, $accent, $svCid = '') {
    $a = ($addr === '') ? '<span style="color:#aab2bf">-</span>' : esc($addr);
    $meta = [];
    if ($floor !== '') { $meta[] = 'Этаж&nbsp;<b style="color:#334155">' . esc($floor) . '</b>'; }
    if ($lift  !== '') { $meta[] = 'Лифт&nbsp;<b style="color:#334155">' . esc($lift) . '</b>'; }
    $metaStr = $meta ? implode('&nbsp;&nbsp;·&nbsp;&nbsp;', $meta) : '';
    return '<td width="50%" valign="top" style="padding:16px 18px;background:#f6f8fb;border:1px solid #e7ecf3;border-radius:12px">'
        . ($svCid !== '' ? '<div style="margin-bottom:11px;border-radius:9px;overflow:hidden;border:1px solid #e2e8f0"><img src="cid:' . $svCid . '" alt="' . esc($title) . '" width="100%" style="display:block;width:100%;height:auto"></div>' : '')
        . '<div style="color:' . $accent . ';font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;margin-bottom:7px">' . esc($title) . '</div>'
        . '<div style="color:#0f172a;font-size:17px;font-weight:800;line-height:1.35">' . $a . '</div>'
        . ($metaStr ? '<div style="color:#64748b;font-size:13px;margin-top:9px">' . $metaStr . '</div>' : '')
        . '</td>';
}
function streetView($addr, $key, $cid) {
    $addr = trim((string)$addr);
    if ($addr === '' || $key === '') { return ['', '']; }
    $meta = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/streetview/metadata?source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key)), true);
    if (!isset($meta['status']) || $meta['status'] !== 'OK') { return ['', '']; }
    $img = fetchUrl('https://maps.googleapis.com/maps/api/streetview?size=560x220&fov=78&source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key));
    if ($img !== '' && (strncmp($img, "\xFF\xD8", 2) === 0 || strncmp($img, "\x89PNG", 4) === 0)) { return [$img, $cid]; }
    return ['', ''];
}
function ok() { echo json_encode(['ok' => true]); exit; }
function fail($code, $err) { http_response_code($code); echo json_encode(['ok' => false, 'error' => $err]); exit; }
