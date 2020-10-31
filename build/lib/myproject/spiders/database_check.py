import sqlite3
conn=sqlite3.connect('MyData.db')
cmp="Titan Company Ltd."
#cursor=conn.execute(f'''SELECT * FROM MYDATA WHERE COMPANY_NAME = '{cmp.lower()}';''')
#cursor=conn.execute('''SELECT DISTINCT COMPANY_NAME FROM MYDATA;''')
#cursor=conn.execute('''SELECT * FROM MYCOMPANY;''')
#cmp_list=[]
#for row in cursor:
#    cmp_list.append(row[0])
#count=0
#for i in cmp_list:
#    print(count)
#    cursor=conn.execute(f'''SELECT * FROM MYDATA WHERE COMPANY_NAME = '{i}';''')
#    for row in cursor:
#        print(row)
#    count+=1
#conn.close()

