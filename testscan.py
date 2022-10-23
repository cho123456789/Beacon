import blescan
import sys
import bluetooth._bluetooth as bluez
va = [[0]*100 for i in range(100)]
ca = [[0]*3 for i in range(3)]
dev_id = 0
def abc():
    i=0
    try:
        sock = bluez.hci_open_dev(dev_id)
        #print("ble thread started")
    except:
        print("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)
    me=0
    i=0
    result=0
    while me<100 :
        returnedList = blescan.parse_events(sock, 10)   
        #print("----------")
        for beacon in returnedList:
            if(ca[0][0] == 0 or ca[0][0] != 0):
                if(beacon.mac == "c8:6c:e5:2b:49:f9"):
                        va[i]= beacon.rssi;
                        #print(i)
                        ca[0][0] = va[i]
                        i=i+1
                               
                    
            if(ca[0][1] == 0 or ca[0][1] != 0):     
                if(beacon.mac == "eb:6f:81:d8:11:2e"):
                        #print("before  " + str(i))
                        va[i]= beacon.rssi;
                        #print(i)
                        ca[0][1] = va[i]
                        #print("2p"+ ca[0][1])
                        i=i+1
                    #me= me-1
            if(ca[1][0] == 0 or ca[1][0] != 0):         
                if(beacon.mac == "ee:e4:19:fe:b3:d3"):
                        #print("before  " + str(i))
                        va[i]= beacon.rssi;
                        #print("3p"+ va[i])
                        #print(i)
                        ca[1][0] = va[i]
                        #print("3p"+ ca[1][0])
                        i=i+1
                    
            if(ca[1][1] == 0 or ca[1][1] != 0):        
                if(beacon.mac == "fe:69:53:e2:fd:77"):
                        #print("  " + str(i))
                        va[i]= beacon.rssi;
                        #print("4p"+ va[i])
                        #print(i)
                        ca[1][1] = va[i]
                        #print("4p"+ ca[1][1])
                        i=i+1
                        
            if(ca[2][0] == 0 or ca[2][0] != 0):
                if(beacon.mac == "e9:11:9f:ce:02:1c"):
                        #print("  " + str(i))
                        va[i]= beacon.rssi;
                        #print("4p"+ va[i])
                        #print(i)
                        ca[2][0] = va[i]
                        #print("4p"+ ca[1][1])
                        i=i+1            
            me=me+1      
            #print(me)
           
            #return ca;  


             
        if(i>=2):
            
         #   print("pi----")
            break;
            
    return ca; 
#if __name__ == "__main__":
    #while True:
        #=if(i >=1):
         #   print("pi----")
           #abc()
            #break;
    