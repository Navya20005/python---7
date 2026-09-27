class Email:
    def send(self, message):
        print("Email:", message)


class SMS:
    def send(self, message):
        print("SMS:", message)


class WhatsApp:
    def send(self, message):
        print("WhatsApp:", message)


def notify(obj):
    obj.send("Hello, this is a notification")


e = Email()
s = SMS()
w = WhatsApp()

notify(e)
notify(s)
notify(w)