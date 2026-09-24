# Part F, Method overriding

# 1. Create a base class Notification with a method send() that returns a general message
class Notification:
    def __init__(self):
        pass

    def send(self):
        return "This is a generic notification!"


# 2. Create EmailNotification(Notification) and SMSNotification(Notification)
# 3. Override send() in both subclasses so each returns a different message
class EmailNotification(Notification):
    def __init__(self):
        super().__init__()

    def send(self):  # Task 3: Overriding base class' send() method
        return "This is an email notification!"


class SMSNotification(Notification):
    def __init__(self):
        super().__init__()

    def send(self):  # Task 3: Overriding base class' send() method
        return "This is a SMS notification!"


# 4. Create one object from each class and call send() on all of them
generic_notification = Notification()
email_notification = EmailNotification()
sms_notification = SMSNotification()

print(generic_notification.send())
print(email_notification.send())
print(sms_notification.send())


# 5. Explain in a comment which method is used when send() is called on each object
# They use their own method, if it exists, if not, they use the base class' method instead