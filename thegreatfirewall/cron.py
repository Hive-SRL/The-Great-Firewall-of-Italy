from django_cron import CronJobBase, Schedule
#
# Scheduler che ogni minuto richiede alla piattaforma Piracy Shield se ci sono nuovi ticket da eleaborare
#
class CheckTicket(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'thegreatfirewall.check_ticket'

    def do(self):
        pass

#Scheduler che controlla la scadenza dei token e ne chiede di nuovi se necessario
class RefreshCredentials(CronJobBase):
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'thegreatfirewall.check_credentials'

    def do(self):
        pass