from pymongo import MongoClient
import gridfs
import redis

# MongoDB Atlas connection URI
MONGO_URI = "mongodb://cmo_admin:Admin_cmo123@cluster0-shard-00-00.ktndx.mongodb.net:27017,cluster0-shard-00-01.ktndx.mongodb.net:27017,cluster0-shard-00-02.ktndx.mongodb.net:27017/?ssl=true&replicaSet=atlas-haei1n-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"


# Connect to MongoDB
client = MongoClient(MONGO_URI)  # ✅ Corrected: Removed quotes around MONGO_URI
db = client["face_recognition_db"]  # Database name

# GridFS setup for storing images
fs = gridfs.GridFS(db)

# Ensure indexes for faster searches
db.image_metadata.create_index([("event", 1)])
db.image_metadata.create_index([("date", 1)])
db.image_metadata.create_index([("face_embeddings", 1)])

# Connect to Redis for caching
redis_client = redis.Redis(host="localhost", port=6379, db=0)

print("✅ MongoDB & Redis Connected & Indexes Created!")
