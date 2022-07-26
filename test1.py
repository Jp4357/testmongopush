import pymongo

client = pymongo.MongoClient("mongodb+srv://test_jp:vrjp4357@cluster0.32c6x7d.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["jp"]

# record = collection.find()
# for i in record:
#     print(i)

#data = collection.find({"companyName":"iNeuron"})
data = collection.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)


