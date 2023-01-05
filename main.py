from datetime import datetime
import pytz # $ pip install pytz
from InquirerPy import inquirer

t = inquirer.select(
    message="Choose a timezone",
    choices=['America/New_York'],
).execute()

tz = pytz.timezone(t)

zt = datetime.now(tz)
ztf = zt.strftime("%H:%M:%S")

print("heure de la zone : "+t)
print(ztf)