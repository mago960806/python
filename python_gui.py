import psycopg2
from tkinter import *

master = Tk()
master.title("4A主账号密码获取")
master.geometry('320x240')
master.resizable(width=False,height=False)

Label(master, text="请输入4A账号：").grid(row=0, sticky = W)
password=variable()
e1 = Entry(master,textvariable=password)
e1.grid(row=0, column=1)
password.get("请输入4A账号")

mainloop()

def get_4a_passwd():
	conn=psycopg2.connect(database="venustech",user="venustech",password="sysadmin@028",host="134.224.126.3",port="5432")
	cursor=conn.cursor()
	cursor.execute("SELECT name,password FROM t_acc_master where name='sxy802102';")
	result=cursor.fetchone()
	print(result[0],"的密码为:",result[1])
	cursor.close()
	conn.close()
