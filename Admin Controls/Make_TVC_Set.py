import datetime
import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


setName = input("Enter the set name (as it appears in firestore): ")
slotCost = int(input("Enter slot cost: "))

print(f'\nReady to make set {setName} with slot cost {slotCost}ICs...')

option = input("Proceed? \nY/n: ")
print("")

if option == "Y":
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    # Gotta make a document field for some reason else firestore don't work :/
    # db.collection('tvc_sets') \
    #     .document(setName) \
    #     .set({"test": "test"})

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
            "timestamp": datetime.datetime.now(),
            "cost": slotCost,
            "slot_duration": timeslot,
            "sequence_index": count,
        }
        db.collection('tvc_sets') \
            .document(setName) \
            .collection('Group_A') \
            .document(data['slot_duration']) \
            .update(data)
        print(f"[+] Made slot for {data['slot_duration']} for {slotCost}ICs for Group A.")
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
            "timestamp": datetime.datetime.now(),
            "cost": slotCost,
            "slot_duration": timeslot,
            "sequence_index": count,
        }
        db.collection('tvc_sets') \
            .document(setName) \
            .collection('Group_B') \
            .document(data['slot_duration']) \
            .update(data)
        print(f"[+] Made slot for {data['slot_duration']} for {slotCost}ICs for Group B.")
        count += 1
    print('\n[+] Program Ended.')
else:
    print('\n[+] Program Ended.')
