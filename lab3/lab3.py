import sqlite3 as sql
import os
import random
import datetime
import logging

logname = "Journal.txt"

logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def check_time_cooldown(time: datetime or None) -> bool:
    if time == None:
        return True
    time_after_three_minutes = time + datetime.timedelta(minutes=3)
    return datetime.datetime.now() > time_after_three_minutes

def gen_rand_list() -> list:
    list_key = []
    for i in range(5):
        list_key.append(random.randint(1000,9999))
    return list_key


def authorizate(cur, con) -> None:
    ADMIN = 777
    USER = 100
    login = input("Login : ")
    passwd = input("Passwd : ")
    statement = f"SELECT * from users2 WHERE username='{login}' AND Password = '{passwd}';"
    cur.execute(statement)
    res = cur.fetchone()
    if not res:
        print("Login failed")
        exit(1)
    else:
        login, _, permition, _, _ = res
        print(f"Welcome {login}\nWrite reg to registration new user\nExit to exit")
        if permition == 1:
            os.system(f"chmod {ADMIN} file_system")
            logging.info("Admin entered")
        else:
            os.system(f"chmod {USER} file_system")
            logging.info("User entered")
        os.chdir("file_system")
        while True:
            com = input(f"{login}: ")
            if com.startswith("sudo"):
                logging.warning("!!!!!!!! Get the admin !!!!!!!!")
            if com.lower() == "exit":
                break
            if com.lower() == "reg" and permition == 1:
                login = input("Login : ")
                passwd = input("Passwd : ")
                perm = input("Perm 1 - admin 0 - user: ")
                str_list_key = ' '.join(gen_rand_list())
                print(f"Your key values:\n{str_list_key}")
                date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                cur.execute("""INSERT INTO "users2" VALUES (?,?,?,?,?);""",
                    (login,passwd,perm,str_list_key,date))
                con.commit()
            cur.execute("SELECT date FROM users2 WHERE username=?",(login,))
            time = cur.fetchone()[0]
            if time != "-":
                time = datetime.datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
                if check_time_cooldown(time):
                    key = input("please input key : ")
                    cur.execute("SELECT list_keys FROM users2 WHERE username=?",(login,))
                    while True:
                        count = 0
                        if key in cur.fetchone()[0]:
                            logging.info(f"Running command {com}")
                            os.system(com)
                            break
                        elif count == 3:
                            exit(1)
                        else:
                            count += 1
                else:
                    logging.info(f"Running command {com}")
                    os.system(com)
            else:
                logging.info(f"Running command {com}")
                os.system(com)

if __name__ == "__main__":
    con = sql.connect("my.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS "users2" (
        "username"  TEXT,
        "password"  TEXT,
        "perm" INTEGER,
        "list_keys" TEXT,
        "date" TEXT
        );""")
    cur.execute("""INSERT INTO "users2" VALUES ('admin','password','1','000','-');""")
    cur.execute("""INSERT INTO "users2" VALUES ('user','123','0','222','-');""")
    con.commit()
    authorizate(cur, con)
