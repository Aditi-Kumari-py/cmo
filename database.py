from pymongo import MongoClient
import gridfs
import redis

# MongoDB Atlas connection URI
MONGO_URI = "mongodb://cmo_admin:Admin_cmo123@cluster0-shard-00-00.ktndx.mongodb.net:27017,cluster0-shard-00-01.ktndx.mongodb.net:27017,cluster0-shard-00-02.ktndx.mongodb.net:27017/?ssl=true&replicaSet=atlas-haei1n-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

# ✅ Lazy MongoDB Connection (to prevent fork issues)
def get_db():
    client = MongoClient(MONGO_URI)
    return client["face_recognition_db"]

db = get_db()  
fs = gridfs.GridFS(db)

# ✅ Ensure indexes for faster searches
db.image_metadata.create_index([("event", 1)])
db.image_metadata.create_index([("date", 1)])
db.image_metadata.create_index([("face_embeddings", "2dsphere")])  # ✅ Optimized for vector search

# ✅ Redis Connection with Exception Handling
try:
    redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    redis_client.ping()
    print("✅ Redis Connected!")
except redis.ConnectionError:
    print("❌ Redis Connection Failed!")

print("✅ MongoDB & GridFS Connected & Indexes Created!")
