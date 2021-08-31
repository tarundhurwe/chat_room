from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import auto_delete

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(auto_delete, 'interval', minutes = 5)
    scheduler.start()