from datetime import datetime
import pytz # $ pip install pytz
from InquirerPy import inquirer


def ask_prompt_time_zone() -> str:
    available_time_zones = ['America/New_York']
    return inquirer.select(
        message="Choose a timezone",
        choices=available_time_zones,
    ).execute()

def generate_zoned_date(time_zone_text:str) -> datetime:
    time_zone = pytz.timezone(time_zone_text)
    zoned_time = datetime.now(time_zone)
    return zoned_time

def format_date(date:datetime) -> str:
    hh_mm_ss_format = "%H:%M:%S"
    return date.strftime(hh_mm_ss_format)

def main():
    time_zone_text = ask_prompt_time_zone()
    zoned_date = generate_zoned_date(time_zone_text)
    print("heure de la zone : "+time_zone_text)
    print(format_date(zoned_date))

if __name__ == "__main__":
    main()