#step 1 install and import pymongo
import pymongo
import pymongo.mongo_client

#step 2 - create a mongodb client
conn_str = "mongodb://localhost:27017/"
try:
    client = pymongo.MongoClient(conn_str)
    print("connection success")
except Exception:
    print("Error:" + Exception)
 
#create
#step 3- create a DB
myDb = client["pymongo_DB"]
 
#step 4 - create a collection
myCollection = myDb["Mydemo_collection"]
print(client.list_database_names())

#step 5 create document
myDoc = {
    "nama cust" : "imam",
    "email" : "imamwahyu@maribelajar.org",
    "umur" : 21,
    "alamat" : "Depok"
}

#step 6 insert document
Myinst = myCollection.insert_one(myDoc)

print(Myinst.inserted_id)
print(client.list_database_names())