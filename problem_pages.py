#!/usr/bin/env python3
"""Build the problem-led repair pages in ET, RU and EN on the service template."""

from problem_content import PROBLEM_ORDER, problem_page
from service_layout import write_service


if __name__ == "__main__":
    count = 0
    for key, _row in PROBLEM_ORDER:
        for lang in ("et", "ru", "en"):
            write_service(lang, problem_page(key, lang))
            count += 1
    print(f"Problem pages done: {count}")
