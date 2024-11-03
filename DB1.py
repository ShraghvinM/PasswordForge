from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
load_dotenv(find_dotenv())

connection_string = f"mongodb+srv://**MONGO_USERNAME**:**MONGO_PASSWORD**@cluster0.nleriea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0-dot"
client = MongoClient(connection_string)
users_db = client.user_credentials
passwords_db = client.user_passwords
users = users_db.users
passwords = passwords_db.passwords


def add_pass(username, password, userid):
    doc = {
        "name": username,
        "key": password
    }
    columns = {"_id": 0, "username": 1, "password":1}
    full_list = list(passwords.find({}, columns))
    u = False
    for i in full_list:
        if (userid == i['username']):
            u = True
    if (u == True):
        query = {'username': userid}
        document = passwords.find_one(query)
        if document:
            password_field = document.get('password', [])
            password_field.append(doc)
            passwords.update_one(query, {"$set": {'password': password_field}})
            return True
        else:
            return False

def delete_pass(username, userid):
    doc = {
        "name": username,
    }
    columns = {"_id": 0, "username": 1, "password":1}
    full_list = list(passwords.find({}, columns))
    u = False
    for i in full_list:
        if (userid == i['username']):
            u = True
    if (u == True):
        query = {'username': userid}
        document = passwords.find_one(query)
        if document:
            password_field = document.get('password', [])
            for i in password_field:
                if (username == i['name']):
                    password_field.remove(i)
            passwords.update_one(query, {"$set": {'password': password_field}})
            return True
        else:
            return False
def edit_pass(username, userid, value):
    doc = {
        "name": username,
        "key": value
    }
    columns = {"_id": 0, "username": 1, "password":1}
    full_list = list(passwords.find({}, columns))
    query = {'username': userid}
    document = passwords.find_one(query)
    if document:
        password_field = document.get('password', [])
        for x in password_field:
            if (username == x['name']):
                exists = True
            else:
                exists = False
    if exists:
        u = False
        for i in full_list:
            if (userid == i['username']):
                u = True
        if (u == True):
            query = {'username': userid}
            document = passwords.find_one(query)
            if document:
                password_field = document.get('password', [])
                for i in password_field:
                    if (username == i['name']):
                        password_field.remove(i)
                password_field.append(doc)
                passwords.update_one(query, {"$set": {'password': password_field}})
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def list_of_passwords(email):
    columns = {"_id": 0, "username": 1, "password":1}
    full_list = list(passwords.find({}, columns))
    if (full_list == []):
        return []
    else:
        for i in full_list:
            if (email == i['username']):
                all = i['password']
        if all:
            rand_stuff = {
                'name': "blank",
                'key' : "blank"
            }
            all.remove(rand_stuff)
            return all
        else:
            return []
        
def register_acc(email, password):
    doc = {
        "email": email,
        "password": password
        
        }
    columns = {"_id": 0, "email": 1, "password":1}
    full_list = list(users.find({}, columns))
    u = False
    for i in full_list:
        if (email == i['email']):
            u = True
    if (u == False):
        users.insert_one(doc)
        pass_doc = {
            "username": email,
            "passwords": {}
        }
        passwords.insert_one(pass_doc)
        doc = {
        "name": "blank",
        "key": "blank"
        }
        columns = {"_id": 0, "username": 1, "password":1}
        full_list = list(passwords.find({}, columns))
        temp_signup = False
        for i in full_list:
            if (email == i['username']):
                temp_signup = True
        if (temp_signup == True):
            query = {'username': email}
            document = passwords.find_one(query)
            if document:
                password_field = document.get('password', [])
                password_field.append(doc)
                passwords.update_one(query, {"$set": {'password': password_field}})
    else:
        return True

def login_acc(email, password):
    doc = {
        "email": email,
        "password": password,
    }
    columns = {"_id": 0, "email": 1, "password":1}
    full_list = list(users.find({}, columns))
    u = False
    for i in full_list:
        if (email == i['email']):
            u = True
    if (doc in full_list):
        p = True
    else:
        p = False
    if (u == False and p == False):
        return 0
    elif (u == True and p == False):
        return 1
    else:
        return 2
