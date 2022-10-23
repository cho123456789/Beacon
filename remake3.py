import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import sys
sys.path.append("/home/pi/BB/scan")
import sys
from testscan import abc
import blescan
import bluetooth._bluetooth as bluez
import subprocess
import struct
import time
import threading
import MySQLdb
import math
cred = credentials.Certificate("./dadasd-fb6dd-firebase-adminsdk-p3gky-f3abb3e4c9.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'raspberry').document(u'raspberry')
db= MySQLdb.connect(host="101.101.216.205",user="chan",passwd="5562",db="test1",port=3306)
cursor = db.cursor()
pi_1_rssi =""
pi_2_rssi =""
pi_3_rssi =""
pi_4_rssi =""
i=0
before_a = [10,20,30]
       
def atfer(fd1,sd1,sd,dic,before_a,p11,p22,p33,p44,p55):
        print("ater")
        ads = sorted(set(before_a))
        print(fd1,sd1)
        #print(str(sd[0])+ str("@"))
        #dic[sd[0]]
        #print(str(dic[sd[0]])+ str("@"))
        print(str(dic[fd1]))
        print(str(dic[sd1]))
        
        if((int(dic[fd1]) == 1 and int(dic[sd1]) == 3) or (int(dic[fd1])== 3 and int(dic[sd1]) == 1) ):     
            sql_2= "SELECT * FROM test1.new_table_type WHERE ID="+"\""+str(dic[fd1]) +"\""+"or ID="+"\""+str(dic[sd1]) +"\""
            cursor.execute(sql_2)
            result2 = cursor.fetchall()
            print(result2)
            for i in range(4):                
                    result3 = result2[0][i]
                    if(int(result3) == int(result2[1][0])):
                        i= i+1
                        before_a.append(2)
                        print(before_a)
                        break
                   
                
        if((int(dic[fd1]) == 1 and int(dic[sd1]) == 7) or (int(dic[fd1])== 7 and int(dic[sd1]) == 1) ):     
            sql_2= "SELECT * FROM test1.new_table_type WHERE ID="+"\""+str(dic[fd1]) +"\""+"or ID="+"\""+str(dic[sd1]) +"\""
            cursor.execute(sql_2)
            result2_4 = cursor.fetchall()
            for i in range(4):
                result4 = result2_4[0][i]
                if(int(result4) == int(result2_4[1][0])):
                    re2 = int(4)
                    print(re2)
                    before_a.append(4)
                    print(before_a)
                    break
        if((int(dic[fd1]) == 3 and int(dic[sd1]) == 9) or (int(dic[fd1])== 9 and int(dic[sd1]) == 3) ):     
            sql_2= "SELECT * FROM test1.new_table_type WHERE ID="+"\""+str(dic[fd1]) +"\""+"or ID="+"\""+str(dic[sd1]) +"\""
            cursor.execute(sql_2)
            result2_4 = cursor.fetchall()
            for i in range(4):
                result4 = result2_4[0][i]
                if(int(result4) == int(result2_4[1][0])):
                    re2 = int(6)
                    print(re2)
                    before_a.append(6)
                    print(before_a)
                    break
              
        if((int(dic[fd1]) == 7 and int(dic[sd1]) == 9) or (int(dic[fd1])== 9 and int(dic[sd1]) == 7) ):     
            sql_2= "SELECT * FROM test1.new_table_type WHERE ID="+"\""+str(dic[fd1]) +"\""+"or ID="+"\""+str(dic[sd1]) +"\""
            cursor.execute(sql_2)
            result2_8 = cursor.fetchall() 
            for i in range(4):
                result4 = result2_8[0][i]
                if(int(result4) == int(result2_8[1][0])):
                    re2 = int(8)
                    print(re2)
                    i= i+1
                    before_a.append(8)
                    print(before_a)
                    break
               
                
        count_2 = before_a.count(2)
        
        #print("2나온 횟수",str(count_2))
        
        count_4 = before_a.count(4)
       
        #print("4나온 횟수",str(count_4))
            
        count_6 = before_a.count(6)
        
        #print("6나온 횟수",str(count_6))
        count_8 = before_a.count(8)
        
        #print("8나온 횟수",str(count_8))
        
     
        print("2나온 횟수",str(count_2))
        print("4나온 횟수",str(count_4))
        print("6나온 횟수",str(count_6))
        print("8나온 횟수",str(count_8))   
            
        if( count_2 >  count_6 and  count_2 >  count_4 and  count_2 > count_8):
            doc_ref.update({
                        u'result2' : int(2)
                    })
            sql_3= "UPDATE test1.new_table_sum SET ID='2',b1=b1+1 WHERE ID='2'"
            cursor.execute(sql_3)
            db.commit()

            count_4=0
                    
                
        elif( count_4 > count_2 and  count_4 >  count_6 and  count_4 > count_8):
          
           doc_ref.update({
                        u'result2' : int(4)
                    })
           sql_3= "UPDATE test1.new_table_sum SET ID='4',b1=b1+1 WHERE ID='4'"
           cursor.execute(sql_3)
           db.commit()
           
        elif( count_6 > count_2 and  count_6 >  count_4 and  count_6 > count_8):
           
           doc_ref.update({
                        u'result2' : int(6)
                    })
           sql_3= "UPDATE test1.new_table_sum SET ID='6',b1=b1+1 WHERE ID='6'"
           cursor.execute(sql_3)
           db.commit()
           
        elif( count_8 > count_2 and  count_8 >  count_6 and  count_8 > count_4):
           
            
           doc_ref.update({
                        u'result2' : int(8)
                    })
           sql_3= "UPDATE test1.new_table_sum SET ID='8',b1=b1+1 WHERE ID='8'"
           cursor.execute(sql_3)
           db.commit()
           
       
        if(count_2 > 7 or count_4 > 7 or count_6 > 7 or count_8 > 7 ):
            before_a.clear()
           
       
        
  


def before(p11,p22,p33,p44,p55):
        print("before")
        pi_1_rssi = str(p11)
        p11s = abs(p11)
        pi_2_rssi = str(p22)
        p22s = abs(p22)
        pi_3_rssi = str(p33)
        p33s = abs(p33)
        pi_4_rssi = str(p44)
        p44s = abs(p44)
        pi_5_rssi = str(p55)
        p55s = abs(p55)
        if((p11s >= 20) and  (p11s < p22s) and (p11s < p33s) and (p11s < p44s) and (p11s < p55s) and p11s < 60):
                sql_2= "SELECT * FROM test1.new_beacon2 WHERE b1 ="+"\""+pi_1_rssi +"\""+"or b2 ="+"\""+pi_1_rssi +"\""+"or b3 ="+"\""+pi_1_rssi +"\""+"or b4 ="+"\""+pi_1_rssi +"\""+"or b5 ="+"\""+pi_1_rssi +"\""+"or b6 ="+"\""+pi_1_rssi +"\""+"or b7 ="+"\""+pi_1_rssi +"\""+"or b8 ="+"\""+pi_1_rssi +"\""+"or b9 ="+"\""+pi_1_rssi +"\""+"or b10 ="+"\""+pi_1_rssi +"\""+"or b11 ="+"\""+pi_1_rssi +"\""+"or b12 ="+"\""+pi_1_rssi +"\""+"or b13 ="+"\""+pi_1_rssi +"\""+"or b14 ="+"\""+pi_1_rssi +"\""+"or b15 ="+"\""+pi_1_rssi +"\""+"or b16 ="+"\""+pi_1_rssi +"\""+"or b17 ="+"\""+pi_1_rssi +"\""+"or b18 ="+"\""+pi_1_rssi +"\""+"or b19 ="+"\""+pi_1_rssi +"\""+"or b20 ="+"\""+pi_1_rssi +"\""+"or b21 ="+"\""+pi_1_rssi+"\""+"or b22 ="+"\""+pi_1_rssi +"\""+"or b23 ="+"\""+pi_1_rssi +"\""+"or b24 ="+"\""+pi_1_rssi +"\""+"or b25 ="+"\""+pi_1_rssi +"\""+"or b26 ="+"\""+pi_1_rssi +"\""+"or b27 ="+"\""+pi_1_rssi +"\""+"or b28 ="+"\""+pi_1_rssi +"\""+"or b29 ="+"\""+pi_1_rssi +"\""+"or b30 ="+"\""+pi_1_rssi +"\""+"or b31 ="+"\""+pi_1_rssi +"\""+"or b32 ="+"\""+pi_1_rssi +"\""+"or b33 ="+"\""+pi_1_rssi +"\""+"or b34 ="+"\""+pi_1_rssi +"\""+"or b35 ="+"\""+pi_1_rssi +"\""+"or b36 ="+"\""+pi_1_rssi +"\""  +"or b37 ="+"\""+pi_1_rssi +"\""+"or b38 ="+"\""+pi_1_rssi +"\""+"or b39 ="+"\""+pi_1_rssi +"\""+"or b40 ="+"\""+pi_1_rssi +"\""    
                #print(sql_2)
                cursor.execute(sql_2)
                result2 = cursor.fetchall()
                #print(result2)
                re = result2[0][0]
                doc_ref.update({
                        u'result2' : int(re)
                })
                before_a.append(re)
                sql_3= "UPDATE test1.new_table_sum SET ID='1',b1=b1+1 WHERE ID='1'"
                cursor.execute(sql_3)
                db.commit()
            
       
        if((p22s >= 20) and  (p22s < p11s) and (p22s < p33s) and (p22s < p44s) and (p22s < p55s) and p22s < 60):
                sql_2= "SELECT * FROM test1.new_beacon3 WHERE b1 ="+"\""+pi_2_rssi +"\""+"or b2 ="+"\""+pi_2_rssi +"\""+"or b3 ="+"\""+pi_2_rssi +"\""+"or b4 ="+"\""+pi_2_rssi +"\""+"or b5 ="+"\""+pi_2_rssi +"\""+"or b6 ="+"\""+pi_2_rssi +"\""+"or b7 ="+"\""+pi_2_rssi +"\""+"or b8 ="+"\""+pi_2_rssi +"\""+"or b9 ="+"\""+pi_2_rssi +"\""+"or b10 ="+"\""+pi_2_rssi +"\""+"or b11 ="+"\""+pi_2_rssi +"\""+"or b12 ="+"\""+pi_2_rssi +"\""+"or b13 ="+"\""+pi_2_rssi +"\""+"or b14 ="+"\""+pi_2_rssi +"\""+"or b15 ="+"\""+pi_2_rssi +"\""+"or b16 ="+"\""+pi_2_rssi +"\""+"or b17 ="+"\""+pi_2_rssi +"\""+"or b18 ="+"\""+pi_2_rssi +"\""+"or b19 ="+"\""+pi_2_rssi +"\""+"or b20 ="+"\""+pi_2_rssi +"\""+"or b21 ="+"\""+pi_2_rssi +"\""+"or b22 ="+"\""+pi_2_rssi +"\""+"or b23 ="+"\""+pi_2_rssi +"\""+"or b24 ="+"\""+pi_2_rssi +"\""+"or b25 ="+"\""+pi_2_rssi +"\""+"or b26 ="+"\""+pi_2_rssi +"\""+"or b27 ="+"\""+pi_2_rssi +"\""+"or b28 ="+"\""+pi_2_rssi +"\""+"or b29 ="+"\""+pi_2_rssi +"\""+"or b30 ="+"\""+pi_2_rssi +"\""+"or b31 ="+"\""+pi_2_rssi +"\""+"or b32 ="+"\""+pi_2_rssi +"\""+"or b33 ="+"\""+pi_2_rssi +"\""+"or b34 ="+"\""+pi_2_rssi +"\""+"or b35 ="+"\""+pi_2_rssi +"\""+"or b36 ="+"\""+pi_2_rssi +"\""+"or b37 ="+"\""+pi_2_rssi +"\""+"or b38 ="+"\""+pi_2_rssi +"\""+"or b39 ="+"\""+pi_2_rssi +"\""+"or b40 ="+"\""+pi_2_rssi +"\""+"or b41 ="+"\""+pi_2_rssi +"\""    
                #print(sql_2)
                cursor.execute(sql_2)
                result2 = cursor.fetchall()
                #print(result2)
                re = result2[0][0]
                doc_ref.update({
                        u'result2' : int(re)
                })
                before_a.append(re)
                sql_3= "UPDATE test1.new_table_sum SET ID='3',b1=b1+1 WHERE ID='3'"
                cursor.execute(sql_3)
                db.commit()
                
       
        if((p33s >= 20) and  (p33s < p11s) and (p33s < p22s) and (p33s < p44s) and (p33s < p55s) and p33s < 60):
                sql_2= "SELECT * FROM test1.new_beacon4 WHERE b1 ="+"\""+pi_3_rssi +"\""+"or b2 ="+"\""+pi_3_rssi +"\""+"or b3 ="+"\""+pi_3_rssi +"\""+"or b4 ="+"\""+pi_3_rssi +"\""+"or b5 ="+"\""+pi_3_rssi +"\""+"or b6 ="+"\""+pi_3_rssi +"\""+"or b7 ="+"\""+pi_3_rssi +"\""+"or b8 ="+"\""+pi_3_rssi +"\""+"or b9 ="+"\""+pi_3_rssi +"\""+"or b10 ="+"\""+pi_3_rssi +"\""+"or b11 ="+"\""+pi_3_rssi +"\""+"or b12 ="+"\""+pi_3_rssi +"\""+"or b13 ="+"\""+pi_3_rssi +"\""+"or b14 ="+"\""+pi_3_rssi +"\""+"or b15 ="+"\""+pi_3_rssi +"\""+"or b16 ="+"\""+pi_3_rssi +"\""+"or b17 ="+"\""+pi_3_rssi +"\""+"or b18 ="+"\""+pi_3_rssi +"\""+"or b19 ="+"\""+pi_3_rssi +"\""+"or b20 ="+"\""+pi_3_rssi +"\""+"or b21 ="+"\""+pi_3_rssi +"\""+"or b22 ="+"\""+pi_3_rssi +"\""+"or b23 ="+"\""+pi_3_rssi +"\""+"or b24 ="+"\""+pi_3_rssi +"\""+"or b25 ="+"\""+pi_3_rssi +"\""+"or b26 ="+"\""+pi_3_rssi +"\""+"or b27 ="+"\""+pi_3_rssi +"\""+"or b28 ="+"\""+pi_3_rssi +"\""+"or b29 ="+"\""+pi_3_rssi +"\""+"or b30 ="+"\""+pi_3_rssi +"\""+"or b31 ="+"\""+pi_3_rssi +"\""+"or b32 ="+"\""+pi_3_rssi +"\""+"or b33 ="+"\""+pi_3_rssi +"\""+"or b34 ="+"\""+pi_3_rssi +"\""+"or b35 ="+"\""+pi_3_rssi +"\""+"or b36 ="+"\""+pi_3_rssi +"\""+"or b37 ="+"\""+pi_3_rssi +"\""+"or b38 ="+"\""+pi_3_rssi +"\""+"or b39 ="+"\""+pi_3_rssi +"\""+"or b40 ="+"\""+pi_3_rssi +"\""+"or b41 ="+"\""+pi_3_rssi +"\""    
                #print(sql_2)
                cursor.execute(sql_2)
                result2 = cursor.fetchall()
                #print(result2)
                re = result2[0][0]
                doc_ref.update({
                        u'result2' : int(re)
                })
               
                before_a.append(re)
                sql_3= "UPDATE test1.new_table_sum SET ID='7',b1=b1+1 WHERE ID='7'"
                cursor.execute(sql_3)
                db.commit()
                
        
        if((p44s >= 20) and  (p44s < p11s) and (p44s < p22s) and (p44s < p33s) and (p44s < p55s) and  p44s < 60 ):
                sql_2= "SELECT * FROM test1.new_beacon5 WHERE b1 ="+"\""+pi_4_rssi +"\""+"or b2 ="+"\""+pi_4_rssi +"\""+"or b3 ="+"\""+pi_4_rssi +"\""+"or b4 ="+"\""+pi_4_rssi +"\""+"or b5 ="+"\""+pi_4_rssi +"\""+"or b6 ="+"\""+pi_4_rssi +"\""+"or b7 ="+"\""+pi_4_rssi +"\""+"or b8 ="+"\""+pi_4_rssi +"\""+"or b9 ="+"\""+pi_4_rssi +"\""+"or b10 ="+"\""+pi_4_rssi +"\""+"or b11 ="+"\""+pi_4_rssi +"\""+"or b12 ="+"\""+pi_4_rssi +"\""+"or b13 ="+"\""+pi_4_rssi +"\""+"or b14 ="+"\""+pi_4_rssi +"\""+"or b15 ="+"\""+pi_4_rssi +"\""+"or b16 ="+"\""+pi_4_rssi +"\""+"or b17 ="+"\""+pi_4_rssi +"\""+"or b18 ="+"\""+pi_4_rssi +"\""+"or b19 ="+"\""+pi_4_rssi +"\""+"or b20 ="+"\""+pi_4_rssi +"\""+"or b21 ="+"\""+pi_4_rssi +"\""+"or b22 ="+"\""+pi_4_rssi +"\""+"or b23 ="+"\""+pi_4_rssi +"\""+"or b24 ="+"\""+pi_4_rssi +"\""+"or b25 ="+"\""+pi_4_rssi +"\""+"or b26 ="+"\""+pi_4_rssi +"\""+"or b27 ="+"\""+pi_4_rssi +"\""+"or b28 ="+"\""+pi_4_rssi +"\""+"or b29 ="+"\""+pi_4_rssi +"\""+"or b30 ="+"\""+pi_4_rssi +"\""+"or b31 ="+"\""+pi_4_rssi +"\""+"or b32 ="+"\""+pi_4_rssi +"\""+"or b33 ="+"\""+pi_4_rssi +"\""+"or b34 ="+"\""+pi_4_rssi +"\""+"or b35 ="+"\""+pi_4_rssi +"\""+"or b36 ="+"\""+pi_4_rssi +"\""+"or b37 ="+"\""+pi_4_rssi +"\""+"or b38 ="+"\""+pi_4_rssi +"\""+"or b39 ="+"\""+pi_4_rssi +"\""+"or b40 ="+"\""+pi_4_rssi +"\""+"or b41 ="+"\""+pi_4_rssi +"\""    
                #print(sql_2)
                cursor.execute(sql_2)
                result2 = cursor.fetchall()
                #print(result2)
                re = result2[0][0]
                #print(re)
                doc_ref.update({
                        u'result2' : int(re)
                })
               
                before_a.append(re)
                sql_3= "UPDATE test1.new_table_sum SET ID='9',b1=b1+1 WHERE ID='9'"
                cursor.execute(sql_3)
                db.commit()
                
        
        if(20 <= p55s <= 30):
                sql_2= "SELECT * FROM test1.new_beacon6 WHERE b1 ="+"\""+pi_5_rssi +"\""+"or b2 ="+"\""+pi_5_rssi +"\""+"or b3 ="+"\""+pi_5_rssi +"\""+"or b4 ="+"\""+pi_5_rssi +"\""+"or b5 ="+"\""+pi_5_rssi +"\""+"or b6 ="+"\""+pi_5_rssi +"\""+"or b7 ="+"\""+pi_5_rssi +"\""+"or b8 ="+"\""+pi_5_rssi +"\""+"or b9 ="+"\""+pi_5_rssi +"\""+"or b10 ="+"\""+pi_5_rssi +"\""+"or b11 ="+"\""+pi_5_rssi +"\""+"or b12 ="+"\""+pi_5_rssi +"\""+"or b13 ="+"\""+pi_5_rssi +"\""+"or b14 ="+"\""+pi_5_rssi +"\""+"or b15 ="+"\""+pi_5_rssi +"\""+"or b16 ="+"\""+pi_5_rssi +"\""+"or b17 ="+"\""+pi_5_rssi +"\""+"or b18 ="+"\""+pi_5_rssi +"\""+"or b19 ="+"\""+pi_5_rssi +"\""+"or b20 ="+"\""+pi_5_rssi +"\""+"or b21 ="+"\""+pi_5_rssi +"\""
                cursor.execute(sql_2)
                result2 = cursor.fetchall()
                #print(result2)
                re = result2[0][0]
                #print(re)
                save1 =re
                doc_ref.update({
                        u'result2' : int(re)
                })
                before_a.append(re)
                sql_3= "UPDATE test1.new_table_sum SET ID='5',b1=b1+1 WHERE ID='5'"
                cursor.execute(sql_3)
                db.commit()
                
        print(before_a)
        my_set = set(before_a) #집합set으로 변환
        new_list = list(my_set)
        ads = sorted(set(new_list))#list로 변환
        
        
def pi():
    print("!!!")
    result2=0
    message = 0
    i=0
    pi = abc()
    while message < 1:
       
        
        print("pi count")
        pi_1_name = "'1p' "
        p1 = str(pi[0][0])
        pi_1_rssi = str(p1)
        print("pi_1 :"+ pi_1_name +  str(pi_1_rssi))
            
        pi_2_name = "'2p' "
        p2 = str(pi[0][1])
        pi_2_rssi = str(p2)
        print("pi_2 :"+ pi_2_name +  str(pi_2_rssi))
            
            
        pi_3_name = "'3p' "
        p3 = str(pi[1][0])
        pi_3_rssi = str(p3)
        print("pi_3 :"+ pi_3_name +  str(pi_3_rssi))
            
            
        pi_4_name = "'4p' "
        p4 = str(pi[1][1])
        pi_4_rssi = str(p4)
        print("pi_4 :"+ pi_4_name +  str(pi_4_rssi))
            
        pi_5_name = "'5p' "
        pi_5_rssi = str(p5)
        print("pi_5 :"+ pi_5_name +  str(pi_5_rssi))
        
        if((p11s == 0 or p11s  >= 80) or (p22s == 0 or p22s  >= 80)or (p33s == 0 or p33s  >= 80) or (p44s == 0 or p44s  >= 80)or(pi_5_rssi == "0" or pi_5_rssi == "-90")):
            pi = abc()     
            
             
        m_1 = p11
        m_2 = p22
        m_3 = p33
        m_4 = p44
        m_5 = p55
        m1=[m_1,m_2,m_3,m_4,m_5]
        #print(m1)
        max_1= m1[0]
        max_2= m1[1]
        max_3= m1[2]
        max_4= m1[3]
        max_5 =m1[4]
            
        
        print("가장 가까운값 1번값 2번 값 추출")
        
 
        
        ad1 = [max_1,max_2,max_3,max_4,max_5]
        sd = sorted(ad1, reverse = True)
        print(sd)
        
        dic = { max_1 : 1 , max_2 : 3, max_3 :7 , max_4 : 9 ,max_5 : 5}
        print(dic)
        fd1 = sd[0]
        sd1 = sd[1]
        
        max_f11= abs(sd[0])
        max_f22 =abs(sd[1])
        print(max_f22,max_f11)
        result_2 = max_f22 -max_f11
        print(result_2)
        if(result_2 >= 4):
            before(p11,p22,p33,p44,p55)
        if (result_2 <= 4):
            atfer(fd1,sd1,sd,dic,before_a,p11,p22,p33,p44,p55)
            
        if ((pi_1_rssi) != "0" and (pi_2_rssi)!= "0" and (pi_3_rssi)!= "0" and (pi_4_rssi) != "0" and (pi_5_rssi) != "0"):  
                 break    
       # db.close()
       
        
if __name__ == "__main__":
   while True:
       if(i==5):
           break
       pi()
       i=i+1
        
    

         

     
    
     
    
#1 app  2 pi
