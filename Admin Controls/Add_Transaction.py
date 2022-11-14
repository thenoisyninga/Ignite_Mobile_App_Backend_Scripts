import datetime
import time

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def AddTransaction(ID, AmountChange, TransactionInfo):

    firestoreData = {
        "Amount": AmountChange,
        "Delegation_ID": ID,
        "Description": TransactionInfo,
        "transaction_time": datetime.datetime.now()
    }

    ICs = db.collection('delegations_ics_balance').where("Delegation_Number", "==", ID).get()
    doc = ICs[0].id
    ICs = ICs[0].to_dict()["Account_Balance"]

    ICs = ICs + int(AmountChange)

    data = {
        'Account_Balance': ICs,
    }
    db.collection('delegations_ics_balance').document(doc).update(data)

    db.collection('ic_transactions').document().set(firestoreData)



print("=====================================================================")
print("====================Add Transaction Program==========================")
print("=====================================================================")

id = input("Input Del ID: ")
amount = input("Input Transaction Amount (to be added): ")
info = input("Enter transaction info: ")

AddTransaction(ID=id, AmountChange=amount, TransactionInfo=info)
print("[+] Transaction Added.")



