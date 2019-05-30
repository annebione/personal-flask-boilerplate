from crontab import CronTab

cron = CronTab(user='username')


job1 = cron.new(command='python /jobs/example1.py')
job1.hour.every(2)

job2 = cron.new(command='python /jobs/example2.py')  
job2.every(6).hours()

for item in cron:  
    print item

cron.write()  