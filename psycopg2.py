import psycopg2
conn=psycopg2.connect(database="venustech",user="venustech",password="sysadmin@028",host="134.224.126.3",port="5432")
cursor=conn.cursor()
cursor.execute("SELECT name,password FROM t_acc_master where name='sxy802102';")
result=cursor.fetchone()
print(result[0],"的密码为:",result[1])
cursor.close()
conn.close()