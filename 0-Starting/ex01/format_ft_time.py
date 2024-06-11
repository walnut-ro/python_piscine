import time
import locale
import datetime


locale.setlocale(locale.LC_ALL, '')

current_time = time.time()
formatted_current_time = locale.format_string("%.4f", current_time, grouping=True)

current_date = datetime.date.today()

print(f"Seconds since January 1, 1970: {formatted_current_time} or {current_time:.2e} in scientific notation")
print(f"{current_date.strftime('%b %d %Y')}")