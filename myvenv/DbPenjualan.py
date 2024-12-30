#Muhammad Imam Wahyudi
#Microsoft Data Engineer

import pymongo
import pymongo.mongo_client

#membuat MongoDB Client
conn_str = "mongodb://localhost:27017/"
try:
    client = pymongo.MongoClient(conn_str)
    print("connection success")
except Exception:
    print("Error:" + Exception)

# 3 membuat DataBase
myDb = client["DB_Penjualan"]

# 4 membuat collection
myCollection = myDb["Perahu"]

# 5 membuat dokumen
myDoc = [
    {
        "Nama" : "Muhammad Imam Wahyudi",
        "NIM" : 202143502546
    },{
        "Price" : "CHF 3337",
        "Boat Type" : "Motor Yacht",
        "Manufacture" : "Rigiflex power boats",
        "Type" : "new boat from stoc",
        "Year Built" : "2017",
        "Lenght" : "4.0",
        "Width" : "1.9",
        "Material" : "Thermoplastic",
        "Location" : "switzerland"
    },{
        "Price" : "EUR 3490",
        "Boat Type" : "Center console boat",
        "Manufacture" : "Terhi power boats",
        "Type" : "new boat from stoc",
        "Year Built" : "2020",
        "Lenght" : "4.0",
        "Width" : "1.5",
        "Material" : "Thermoplastic",
        "Location" : "Germany"
    },{
        "Price" : "CHF 3770",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Terhi power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2020",
        "Lenght" : "4.0",
        "Width" : "1.5",
        "Material" : "Thermoplastic",
        "Location" : "Germany"
    },{
        "Price" : "DKK 25900",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Pioner power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2020",
        "Lenght" : "3.0",
        "Width" : "1.0",
        "Material" : "Thermoplastic",
        "Location" : "Denmark"
    },{
        "Price" : "EUR 3399",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Linder power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2019",
        "Lenght" : "3.55",
        "Width" : "1.46",
        "Material" : "Alumunium",
        "Location" : "Germany"
    },{
        "Price" : "CHF 3650",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Linder power boats",
        "Type" : "new boat from stock",
        "Year Built" : "0",
        "Lenght" : "4.03",
        "Width" : "1.56",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "CHF 3600",
        "Boat Type" : "-",
        "Manufacture" : "Catamaran",
        "Type" : "Used boat,Unleaded",
        "Year Built" : "1999",
        "Lenght" : "6.2",
        "Width" : "2.38",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "DKK 24800",
        "Boat Type" : "Sport Board",
        "Manufacture" : "Catamaran",
        "Type" : "Used boat",
        "Year Built" : "-",
        "Lenght" : "6.2",
        "Width" : "2.38",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "EUR 3333",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Crescent power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2019",
        "Lenght" : "3.64",
        "Width" : "1.37",
        "Material" : "-",
        "Location" : "Germany"
    },{
        "Price" : "EUR 3300",
        "Boat Type" : "Pontoon Boat",
        "Manufacture" : "Whaly power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2018",
        "Lenght" : "4.35",
        "Width" : "1.73",
        "Material" : "-",
        "Location" : "italy"
    },{
        "Price" : "CHF 3500",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Terhi power boats",
        "Type" : "Used boat,Electric",
        "Year Built" : "1987",
        "Lenght" : "4.35",
        "Width" : "1.75",
        "Material" : "GRP",
        "Location" : "Switzerland"
    },{
        "Price" : "CHF 3480",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Marine power boats",
        "Type" : "new boat from stock",
        "Year Built" : "0",
        "Lenght" : "4.13",
        "Width" : "1.41",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "EUR 3500",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "GS Nautica power boats",
        "Type" : "Used boat",
        "Year Built" : "2004",
        "Lenght" : "4.7",
        "Width" : "2.0",
        "Material" : "GRP",
        "Location" : "italy"
    },{
        "Price" : "CHF 4600",
        "Boat Type" : "Runabout",
        "Manufacture" : "Kimple power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2020",
        "Lenght" : "4.4",
        "Width" : "1.65",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "CHF 4500",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Italmarine power boats",
        "Type" : "Used boat,Unleaded",
        "Year Built" : "1997",
        "Lenght" : "3.72",
        "Width" : "1.33",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "CHF 4400",
        "Boat Type" : "Deck Boat",
        "Manufacture" : "Buster power boats",
        "Type" : "new boat from stock,Unleaded",
        "Year Built" : "0",
        "Lenght" : "3.88",
        "Width" : "1.49",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "CHF 4380",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Linder power boats",
        "Type" : "new boat from stock",
        "Year Built" : "0",
        "Lenght" : "4.31",
        "Width" : "1.64",
        "Material" : "Alumunium",
        "Location" : "Switzerland"
    },{
        "Price" : "DKK 30000",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "-",
        "Type" : "Used boat",
        "Year Built" : "1985",
        "Lenght" : "4.0",
        "Width" : "1.0",
        "Material" : "-",
        "Location" : "Denmark"
    },{
        "Price" : "EUR 4000",
        "Boat Type" : "Pilothouse",
        "Manufacture" : "teau power boats",
        "Type" : "Used boat,Diesel",
        "Year Built" : "1981",
        "Lenght" : "8.0",
        "Width" : "2.84",
        "Material" : "PVC",
        "Location" : "France"
    },{
        "Price" : "EUR 4000",
        "Boat Type" : "Cabin Boat",
        "Manufacture" : "-",
        "Type" : "Used boat,Unleaded",
        "Year Built" : "2011",
        "Lenght" : "6.37",
        "Width" : "2.31",
        "Material" : "GRP",
        "Location" : "Germany"
    },{
        "Price" : "EUR 3999",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Linder power boats",
        "Type" : "new boat from stock",
        "Year Built" : "2019",
        "Lenght" : "3.55",
        "Width" : "1.46",
        "Material" : "Alumunium",
        "Location" : "Germany"
    },{
        "Price" : "CHF 4267",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Quicksilver (Brunswick Marine) power boats",
        "Type" : "new boat from stock,Unleaded",
        "Year Built" : "0",
        "Lenght" : "3.78",
        "Width" : "1.71",
        "Material" : "GRP",
        "Location" : "Switzerland"
    },{
        "Price" : "EUR 3930",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Linder power boats",
        "Type" : "new boat from stock,Unleaded",
        "Year Built" : "2020",
        "Lenght" : "4.31",
        "Width" : "1.61",
        "Material" : "Alumunium",
        "Location" : "Germany"
    },{
        "Price" : "EUR 3900",
        "Boat Type" : "Sport Boat",
        "Manufacture" : "Kammin power boats",
        "Type" : "Used boat,Unleaded",
        "Year Built" : "1979",
        "Lenght" : "5.6",
        "Width" : "2.1",
        "Material" : "GRP",
        "Location" : "Germany"
    },{
        "Price" : "CHF 4200",
        "Boat Type" : "Fishing Boat",
        "Manufacture" : "Bucher power boats",
        "Type" : "Used boat,Unleaded",
        "Year Built" : "1998",
        "Lenght" : "5.7",
        "Width" : "1.55",
        "Material" : "GRP",
        "Location" : "Switzerland"
    }
]

# 6 Insert Dokumen
Myinst = myCollection.insert_many(myDoc)

# 7 read dokumen
record = myCollection.find_one()
print(record)

# 8 mencari dokumen
results = myCollection.find({"Boat Type": "Sport Boat"})
for Perahu in results:
    print(Perahu)

# 9 update dokumen
Update_doc = myCollection.find({"Boat Type":"Fishing Boat"}).skip(10).limit(14)

for myDoc in Update_doc:
    myCollection.update_one({"_id": myDoc["_id"]},{"$set": {"Boat Type": "Sport Boat"}})

Update_doc = myCollection.find({"Boat Type": "Sport Boat"}).skip(10).limit(14)
for myDoc in Update_doc:
    print(myDoc)

# 10 menghapus dokumen ke 24
del_doc = {
    "Price" : "CHF 4200",
    "Boat Type" : "Fishing Boat",
    "Manufacture" : "Bucher power boats",
    "Type" : "Used boat,Unleaded",
    "Year Built" : "1998",
    "Lenght" : "5.7",
    "Width" : "1.55",
    "Material" : "GRP",
    "Location" : "Switzerland"
    }
record_delete = myCollection.delete_one(del_doc)
record_delete = myCollection.find_one()
print(record_delete)

#step 11 close connection
client = pymongo.MongoClient()
client.close()



