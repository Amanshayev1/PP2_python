from datetime import datetime, timedelta

now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print(without_microseconds)
