import pymongo
import pymongo.mongo_client

#membuat MongoDB Client
client = pymongo.MongoClient("mongodb://localhost:27017/") 
db = client["Tugas4"]  #nama database
collection = db["DB_Medals"]  #nama koleksi 

documents = list(collection.find().limit(30))

# Pilih 15 dokumen dengan indeks genap
documents_to_delete = [documents[i] for i in range(30) if i % 2 == 0]

# Hapus dokumen-dokumen yang dipilih
for doc in documents_to_delete:
    collection.delete_one({"_id": doc["_id"]})

print(f"Deleted {len(documents_to_delete)} documents.")

#1. Tambah Config Server
sh.addShard("config01.example.net:27019");
sh.addShard("config02.example.net:27019");
sh.addShard("config03.example.net:27019");

#2. Tambah Shard
sh.addShard("shard01.example.net:27018");
sh.addShard("shard02.example.net:27018");
sh.addShard("shard03.example.net:27018");

#3. Aktifkan Sharding pada Database
sh.enableSharding("Tugas4");

#4. Buat Index Sharding pada Koleksi
sh.shardCollection("Tugas4.DB_Medals", { shardKey: 1 });