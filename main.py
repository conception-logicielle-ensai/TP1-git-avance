from datetime import datetime
import pytz # $ pip install pytz

timezone = pytz.timezone('America/New_York')
current_time = datetime.now(timezone)
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted)