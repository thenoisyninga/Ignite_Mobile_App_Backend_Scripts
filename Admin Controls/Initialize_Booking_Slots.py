import datetime

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    'Room_Name': 'Green_Screen_Room',
    }

slotsList = {
    "timeDuration": "03:00-03:15",
    "isBooked": False,
    "booketAt": datetime.datetime(2022, 1, 5, 15, 0, 00, 0000)
}

#db.collection('tvc_booking').document().set(data)

docs = db.collection('tvc_booking').where('Room_Name', '==', "Green_Screen_Room").get()
docID = docs[0].id

db.collection('tvc_booking').document(docID).collection('Booking_Slots').document().set(slotsList)
db.collection('tvc_booking').document(docID).collection('Booking_Slots').document().set(slotsList)