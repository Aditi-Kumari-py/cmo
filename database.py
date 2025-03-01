from pymongo import MongoClient
import gridfs
import redis

# MongoDB Atlas connection URI
MONGO_URI = "mongodb+srv://cmo_admin:Admin_cmo123@cluster0.mongodb.net/face_recognition_db?retryWrites=true&w=majority"

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
