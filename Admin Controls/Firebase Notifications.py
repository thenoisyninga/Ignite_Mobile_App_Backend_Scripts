import datetime
import time

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials, messaging

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def SendNotificationToDelegates(NotificationTitle, NotificationBody, sendAtTime, data=None):
    print("\nSending Notification...")
    if data is not None:
        del_notification = messaging.Message(
            notification=messaging.Notification(
                title=NotificationTitle,
                body=NotificationBody,
            ),
            topic="delegations",
            data=data
        )
    else:
        del_notification = messaging.Message(
            notification=messaging.Notification(
                title=NotificationTitle,
                body=NotificationBody,
            ),
            topic="delegations",
        )
    if sendAtTime == "now":
        print("Sending Notification...")
        messaging.send(del_notification)
    else:
        while True:
            if sendAtTime <= datetime.datetime.now():
                messaging.send(del_notification)
                break
            else:
                print(f"\n[+] Notification Scheduled to send at {sendAtTime}.")
                time.sleep(2)

    if sendAtTime == "now":
        sendAtTime = datetime.datetime.now()

    firestoreData = {
        "title": NotificationTitle,
        "body": NotificationBody,
        "timestamp": sendAtTime,
    }

    db.collection('notifications').document().set(firestoreData)

    print(f"\n[+] Notification '{NotificationTitle}' Successfully Sent and Recorded.")


title = input("Enter Notification Title: ")
body = input("Enter Notification Body: ")
print("\n\n[1] Send the notfication now.\n[2] Schedule the notification.")
option = int(input("Enter your choice: "))

while True:
    if option == 1:
        timestamp = datetime.datetime.now()
        break
    elif option == 2:
        year = int(input("Enter the year to send the notification in: "))
        month = int(input("Enter the month to send the notification in (January => 1 and so on): "))
        day = int(input("Enter the day to send the notification on: "))
        hour = int(input("Enter the hour to send the notification in (24-hour format): "))
        minute = int(input("Enter the minute to send the notification in: "))
        second = int(input("Enter the second to send the notification in 0_0: "))
        timestamp = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        print(timestamp)
        break
    else:
        print("\nOption doesn't exist...\n")
print("")
print("")
print("")
print(f"title: {title}")
print(f"body: {body}")
if option == 2:
    print(f"Scheduled at {timestamp}")

print("\nConfirm Sending this Notificaion?")
input("[+] Press enter to proceed or close the program to cancel: ")

SendNotificationToDelegates(
    NotificationTitle=title,
    NotificationBody=body,
    sendAtTime=timestamp,
    data= {
        "route": "/notifications"
    },
    # sendAtTime="now"
)
