import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import random

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Password Generation...
def generate_pass():
    generated_pass = ''
    for _ in range(10):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        generated_pass += (chr(random_integer))
    return generated_pass


# Registering Delegations...
for delNum in range(1, 51):
    if delNum == 1:
        delNum = "01"
    elif delNum == 2:
        delNum = "02"
    elif delNum == 3:
        delNum = "03"
    elif delNum == 4:
        delNum = "04"
    elif delNum == 5:
        delNum = "05"
    elif delNum == 6:
        delNum = "06"
    elif delNum == 7:
        delNum = "07"
    elif delNum == 8:
        delNum = "08"
    elif delNum == 9:
        delNum = "09"
    else:
        delNum = str(delNum)

    data = {
        'Head_Del_Password': generate_pass(),
    }
    doc = db.collection('delegations_list').where('Delegation_Number', "==", delNum).get()
    id = doc[0].id
    db.collection('delegations_list').document(id).update(data)
