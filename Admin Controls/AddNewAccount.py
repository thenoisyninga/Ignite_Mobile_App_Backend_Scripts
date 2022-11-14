import random
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


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


delNum = input('Enter A New Delegation Number in 2 digits: ')
group = input('Enter a group (A or B): ')

db = firestore.client()

print('\nRegistering a User and Password...')

delPass = generate_pass()
headPass = generate_pass()

data = {
    'Delegation_Number': delNum,
    'Password': delPass,
    'Head_Del_Password': headPass,
}

db.collection('delegations_list').document().set(data)

print('Done.')

data = {
    'Group': group
}

db.collection('delegation_group_division').document(delNum).set(data)
print(f"\n[+] Registered to Group {group}")

data = {
    'Account_Balance': 1000,
    'Delegation_Number': delNum,
}

db.collection('delegations_ics_balance').document().set(data)

print(f"\n[+] Registered an IC Account")

