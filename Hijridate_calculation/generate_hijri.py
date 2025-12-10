# generate_hijri.py
from hijridate import Gregorian
from datetime import datetime
import pytz
import json
import os

# ফাইল সেভের সঠিক absolute path
OUTPUT_DIR = os.path.join(os.getcwd(), "Hijridate_calculation")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "today_hijri.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 👉 Bangladesh TimeZone
bd_tz = pytz.timezone("Asia/Dhaka")
today = datetime.now(bd_tz)

# আজকের গ্রেগরিয়ান তারিখ
g_year = today.year
g_month = today.month
g_day = today.day

# হিজরীতে কনভার্ট (Umm al-Qura)
hijri = Gregorian(g_year, g_month, g_day).to_hijri()

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

# JSON ফাইলে সেভ করা
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("today_hijri.json সফলভাবে আপডেট হয়েছে!")
print(f"হিজরী তারিখ: {hijri.day} {month_bn} {hijri.year}")
