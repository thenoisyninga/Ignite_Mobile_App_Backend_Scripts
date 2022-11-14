import datetime
import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


GroupListA = [
    '29',
    '31',
    '08',
    '34',
    '47',
    '46',
    '43',
    '01',
    '11',
    '14',
    '49',
    '38',
    '25',
    '45',
    '12',
    '10',
    '33',
    '26',
    '02',
    '42',
    '15',
    '04',
    '50',
    '07',
    '32',
]

GroupListB = [
    '17',
    '06',
    '27',
    '05',
    '39',
    '35',
    '40',
    '37',
    '36',
    '30',
    '23',
    '44',
    '21',
    '41',
    '18',
    '16',
    '13',
    '09',
    '28',
    '48',
    '03',
    '20',
    '22',
    '19',
    '24',
]

for delID in GroupListA:
    db.collection('delegation_group_division').document(delID).set({'Group': "A"})

for delID in GroupListB:
    db.collection('delegation_group_division').document(delID).set({'Group': "B"})
