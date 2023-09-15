import mysql.connector


try:
    db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root123', database = 'users')
except:
    print("Could Not Connect to Database!")
    quit()


crsr = db.cursor()

# Login Function
def login(username, password):
    crsr.execute(f"select * from login_details where user_id = '{username}'")
    details =  crsr.fetchall()
    if(len(details) == 0):
        return False
    else:
        if(details[0][1] == password):
            return True
        else:
            return False

# signUP Function
def signUP(username, password):
    try:
        crsr.execute(f"insert into login_details values('{username}', '{password}')")
        if(crsr.rowcount == 1):
            db.commit()
            return True
        else:
            return False

    except:
        return False

def change(username, password, new_password):
    try:
        crsr.execute(f"update login_details set password = '{new_password}' where user_id = '{username}' and password = '{password}'")
        if(crsr.rowcount == 1):
            db.commit()
            return True
        else:
            return False
    except:
        return False
