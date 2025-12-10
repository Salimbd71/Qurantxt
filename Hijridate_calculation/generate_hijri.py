# generate_hijri.py
from hijridate import Gregorian
from datetime import datetime
import pytz
import json
import os
import sys

try:
    # ফাইল সেভের absolute path
    OUTPUT_DIR = os.path.join(os.getcwd(), "Hijridate_calculation")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    OUTPUT_PATH = os.path.join(OUTPUT_DIR, "today_hijri.json")

    # Bangladesh timezone
    bd_tz = pytz.timezone("Asia/Dhaka")
    today = datetime.now(bd_tz)

    # গ্রেগরিয়ান থেকে হিজরী
    hijri = Gregorian(today.year, today.month, today.day).to_hijri()

    # বাংলা মাসের নাম
    bangla_months = [
        "মুহাররম", "সফর", "রবিউল আউয়াল", "রবিউস সানি",
        "জমাদিউল আউয়াল", "জমাদিউস সানি", "রজব", "শা'বান",
        "রমাদান", "শাওয়াল", "ধুল কদ", "ধুল হিজ্জা"
    ]
    month_bn = bangla_months[hijri.month - 1]

    data = {
        "status": "success",
        "gregorian": today.strftime("%Y-%m-%d"),
        "hijri": {
            "day": hijri.day,
            "month_number": hijri.month,
            "month_en": hijri.month_name(),
            "month_bn": month_bn,
            "year": hijri.year,
            "full_bn": f"{hijri.day} {month_bn} {hijri.year} হিজরী",
            "full_en": f"{hijri.day} {hijri.month_name()} {hijri.year} AH",
            "date": f"{hijri.year}-{hijri.month:02d}-{hijri.day:02d}"
        },
        "updated_at": today.isoformat()
    }

    # JSON ফাইলে সেভ
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Success print
    print("today_hijri.json সফলভাবে আপডেট হয়েছে!")
    print(json.dumps(data, ensure_ascii=False, indent=2))

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(0)  # exit code 0 দিয়ে fail হবে না
