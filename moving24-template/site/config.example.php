<?php
/* config.example.php  ->  СКОПИРУЙ в config.php и впиши реальные значения.
   config.php НИКОГДА не коммитить и не заливать в публичный доступ.
   lead.php читает эти ключи и шлёт письмо-заявку через Gmail SMTP (PHPMailer). */
return [
  'gmail_user'         => 'sender@gmail.com',      // Gmail-аккаунт-отправитель (SMTP)
  'gmail_app_password' => 'xxxx xxxx xxxx xxxx',    // App Password Gmail (НЕ обычный пароль): myaccount.google.com/apppasswords
  'lead_to'            => 'leads@yourbusiness.ee',  // куда падают заявки
  'maps_key'           => '',                        // (опц.) Google Maps API key для карты маршрута в письме. Пусто = без карты.
];
