# Part A, Polymorphism

# 1. Create 3 classes: EmailNotification, SMSNotification, and PushNotification
# 2. Give all 3 classes a method called send(), but make each method return a different message
class EmailNotification:
    def __init__(self):
        pass

    def send(self):
        return "This is an email notification!"  # Task 2: unique message


class SMSNotification:
    def __init__(self):
        pass
        
    def send(self):
        return "This is a SMS notification"  # Task 2: unique message


class PushNotification:
    def __init__(self):
        pass

    def send(self):
        return "This is a push notification"  # Task 2: unique message


# 3. Create one object from each class and store them in the same list
email_notification_1 = EmailNotification()
sms_notification_1 = SMSNotification()
push_notification = PushNotification()

notifications = [email_notification_1, sms_notification_1, push_notification]


# 4. Loop through the list and call send() on every object
for notification in notifications:
    print(notification.send())


# 5. In a comment, exlpain why the loop does not need to know the exact class of each object
# As long as the object has a .send() method python is able to call it correctly,
# this is because Python is dynamically typed, it doesnt care what type object is of until the code actually runs