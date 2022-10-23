import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import google
import subprocess
import time
import threading

cred = credentials.Certificate("./dadasd-fb6dd-firebase-adminsdk-p3gky-cde10edc79.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getTemp():
    doc_ref = db.collection(u'beacon').document(u'beacon')

    try:
        doc = doc_ref.get()
        aa = u'{}'.format(doc.to_dict())
        bb = u'{}'.format(doc.to_dict())
        cc = u'{}'.format(doc.to_dict())
        dd = u'{}'.format(doc.to_dict())
        #print(aa)
        #print(u'Document data: {}'.format(doc.to_dict()))
        #print(aa)
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
    #threading.Timer(10,getTemp).start()
    return aa;
i=0
while True:
    if(i>=1):
        break;
    getTemp()
    i+=1 
    
