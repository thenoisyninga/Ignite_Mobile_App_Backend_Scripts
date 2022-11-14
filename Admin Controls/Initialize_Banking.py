import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#
# for delNum in range(41, 51):
#     if delNum == 1:
#         delNum = "01"
#     elif delNum == 2:
#         delNum = "02"
#     elif delNum == 3:
#         delNum = "03"
#     elif delNum == 4:
#         delNum = "04"
#     elif delNum == 5:
#         delNum = "05"
#     elif delNum == 6:
#         delNum = "06"
#     elif delNum == 7:
#         delNum = "07"
#     elif delNum == 8:
#         delNum = "08"
#     elif delNum == 9:
#         delNum = "09"
#     else:
#         delNum = str(delNum)
#
#     data = {
#         'Delegation_Number': delNum,
#         'Account_Balance': 0,
#     }
#     db.collection('delegations_ics_balance').document().set(data)


def addTVCSet(setName,):

    timeslotListA = [
        '09:30AM - 09:45AM',
        '09:45AM - 10:00AM',
        '10:00AM - 10:15AM',
        '10:15AM - 10:30AM',
        '10:30AM - 10:45AM',
        '10:45AM - 11:00AM',
        '11:00AM - 11:15AM',
        '11:15AM - 11:30AM',
    ]

    timeslotListB = [
        '03:00PM - 03:15PM',
        '03:15PM - 03:30PM',
        '03:30PM - 03:45PM',
        '03:45PM - 04:00PM',
        '04:00PM - 04:15PM',
        '04:15PM - 04:30PM',
        '04:30PM - 04:45PM',
        '04:45PM - 05:00PM',
    ]

    db = firestore.client()
    for count in range(8):

        data = {
            "time_slot": timeslotListA[count],
            "booked_by_del": '00',
            "cost": 30
        }

        db.collection('tvc_booking').collection(setName).collection('Group_A').document().set(data)

        data = {
            "time_slot": timeslotListB[count],
            "booked_by_del": '00',
            "cost": 30
        }

        db.collection('tvc_booking').doc('tvc_booking').collection(setName).doc(setName).collection('Group_B').document().set(data)


addTVCSet("NewsRoom")