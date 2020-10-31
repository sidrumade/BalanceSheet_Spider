# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class MyprojectPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.con=sqlite3.connect("MyData.db")
    def create_table(self):
        self.con.execute('''DROP TABLE IF EXISTS MYDATA;''')
        self.con.execute('''CREATE TABLE MYDATA(COMPANY_NAME VARCHAR,TOTAL_SHARE_CAPITAL REAL,RESERVES REAL,NET_WORTH REAL,TOTAL_DEBT REAL,YEARS VARCHAR);''')

    def insert_data(self,data_dict):
        cmp_name=data_dict['cmp_name'][0]
        for i in range(5):
            A=data_dict['tsc'][i]
            B=data_dict['res'][i]
            C=data_dict['net'][i]
            D=data_dict['debt'][i]
            E=data_dict['years'][i]
            print(cmp_name,A,B,C,D,E)
            self.con.execute(f'''INSERT INTO MYDATA VALUES("{cmp_name}",{A},{B},{C},{D},"{E}");''')
        self.con.commit()
        

    def process_item(self, item, spider):
        print('pipline data is ',item)
        self.insert_data(item)
        return item
    
class MyprojectPipeline2:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.con=sqlite3.connect("MyData.db")
    def create_table(self):
        self.con.execute('''DROP TABLE IF EXISTS MYCOMPANY;''')
        self.con.execute('''CREATE TABLE MYCOMPANY(COMPANY_NAME VARCHAR);''')
    def insert_data(self,data_dict):
        for i in data_dict['cmp_list']:
            self.con.execute(f'''INSERT INTO MYCOMPANY VALUES("{i}");''')
        self.con.commit()
    def check_new(self,data_dict):
        c=sqlite3.connect('MyDataOld.db')
        cur=c.execute('''SELECT * FROM MYCOMPANY;''')
        old=[]
        for row in cur:
            old.append(row[0])
        c.close()
        new=data_dict['cmp_list']
        f=open('Extra.txt','w')
        for i in new:
            if i not in old:
                print("new company occurs..................................................................",i)
                f.write(str(i))
                f.write("\n")
        f.close()


    def process_item(self, item, spider):
        self.insert_data(item)
        self.check_new(item)
        return item
