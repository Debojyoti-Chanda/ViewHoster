import schedule
import threading
import time

from app.utils import take_screenshot, delete_old_screenshots

# Schedule tasks
schedule.every(20).seconds.do(take_screenshot)
schedule.every(1).minutes.do(delete_old_screenshots)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
