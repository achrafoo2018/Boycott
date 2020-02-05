import schedule
import time
def weekMailSend():
    users = User.objects.all()
    for user in users:
        send_mail("slm", "Hello", settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

schedule.every().wednesday.at("14:58").do(weekMailSend)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
