from datetime import datetime
from zoneinfo import ZoneInfo

def timestamp_to_ny_time(timestamp_ms):
    return datetime.fromtimestamp(timestamp_ms / 1000, ZoneInfo("America/New_York")).strftime('%Y-%m-%d %H:%M:%S')

# Example Test
ts = 1755013818000
print(timestamp_to_ny_time(ts))