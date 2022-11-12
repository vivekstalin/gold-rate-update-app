from apscheduler.schedulers.blocking import BlockingScheduler
from goldPrice import getGoldPrice
sched = BlockingScheduler()

#Time in UTC - IST
sched.add_job(getGoldPrice, 'cron', day_of_week='*', hour='5,11', minute='30')

sched.start()