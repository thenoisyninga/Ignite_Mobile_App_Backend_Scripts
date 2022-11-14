import datetime
import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def InitializeSet(setName):
    # list of group A timeslots
    timeslotListA = [
        '10:50AM - 11:00AM',
        '11:00AM - 11:10AM',
        '11:10AM - 11:20AM',
        '11:20AM - 11:30AM',
        '11:30AM - 11:40AM',
        '11:40AM - 11:50AM',
        '11:50AM - 12:00PM',
    ]

    # Making Slots for Group A
    count = 0
    for timeslot in timeslotListA:
        data = {
            "delID": "00",
        }
        db.collection('tvc_sets') \
            .document(setName) \
            .collection('Group_A') \
            .document(timeslot) \
            .update(data)
        count += 1

    # List of group B timeslots
    timeslotListB = [
        '02:20PM - 02:30PM',
        '02:30PM - 02:40PM',
        '02:40PM - 02:50PM',
        '02:50PM - 03:00PM',
        '03:00PM - 03:10PM',
        '03:10PM - 03:20PM',
        '03:20PM - 03:30PM',
    ]

    # Making Slots for Group B
    count = 0
    for timeslot in timeslotListB:
        data = {
            "delID": "00",
        }
        db.collection('tvc_sets') \
            .document(setName) \
            .collection('Group_B') \
            .document(timeslot) \
            .update(data)
        count += 1
    print(f'\n[+] {setName} slots initialized.')


setNameList = [
    'bank',
    'classroom',
    'fashion_ramp',
    'green_screen_room',
    'hospital',
    'news_room_and_computer_lab',
    'restaurant',
    'science_lab',
    'sports_room',
]

for Set in setNameList:
    InitializeSet(Set)
