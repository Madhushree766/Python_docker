from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# way to connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    client.server_info()  # Test MongoDB connection
    db = client["abc_college"]
    collection = db["registrations"]  
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(" MongoDB Connection Error:", e)
    collection = None  # Set collection to None if connection fails

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    try:
        if collection is None:
            return jsonify({"error": "Database connection failed!"}), 500

        data = request.form
        user_data = {
            "name": data.get("name"),
            "email": data.get("email"),
            "course": data.get("course"),
        }

        collection.insert_one(user_data)
        return jsonify({"message": "Registration Successful!"})

    except Exception as e:
        print(" Error inserting data:", e)
        return jsonify({"error": "Failed to register"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
