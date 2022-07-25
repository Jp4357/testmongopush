
import pymongo
client = pymongo.MongoClient("mongodb+srv://test_jp:vrjp4357@cluster0.32c6x7d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name":"jp",
    "email" : "jp@gmail.com",
    "surname" : "Lenka"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )