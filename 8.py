#
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


def send_notification(notification):
    notification.send()


e = EmailNotification()
s = SMSNotification()
p = PushNotification()

send_notification(e)
send_notification(s)
send_notification(p)