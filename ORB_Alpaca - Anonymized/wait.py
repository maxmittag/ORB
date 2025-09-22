import datetime
import time

def wait_until(target_hour: int, target_minute: int, target_second: int = 0):
    now = datetime.datetime.now()
    start_time = now.replace(
        hour=target_hour, minute=target_minute, second=target_second, microsecond=0
    )
    sleep_seconds = (start_time - now).total_seconds()
    print(f"Warte {sleep_seconds:.0f} Sekunden bis {start_time.strftime('%H:%M:%S')}")
    # Sleep long once
    if sleep_seconds > 1:
        time.sleep(sleep_seconds - 0.5)
    # fintune
    while datetime.datetime.now() < start_time:
        time.sleep(0.01)
        
        
#wait_until(16, 17, 10)
