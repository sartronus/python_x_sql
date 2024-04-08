import mysql.connector


db=mysql.connector.connect(
#    host='enter host here',
#    user='enter user here',
#    password='enter your sql password here',
#    port='enetr port here it should be 3306 by default',
#    database='enter data base in which you have made table in which you want data to be stored'
)
try:
    userid = input("enter id: ")
    username = input("enter name: ")
    password = input("enter password: ")
    ph_no = input("enter phone no.: ")

    courser=db.cursor()

    SQL= 'insert into users (userid,username,password,ph_no) values (%s,%s,%s,%s)'
    sql2='import * from users'
    val=(userid,username,password,ph_no)

    courser.execute(SQL,val)
    courser.execute(sql2)

    db.commit()

except Exception as e:
    print(e)
    db.rollback()

finally:
    db.close()
