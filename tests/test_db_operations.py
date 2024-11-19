import pytest
from pymongo import MongoClient

# Test MongoDB connection with a ping
def test_mongodb_connection():
    try:
        client = MongoClient('mongodb+srv://<username>:<password>@cluster0.mongodb.net/test')
        # Replace <username> and <password> with test credentials or mock them
        client.admin.command('ping')  # Pinging the server
        assert True  # If ping is successful, pass the test
    except Exception as e:
        pytest.fail(f"MongoDB connection test failed: {e}")

        # tests/test_db_operations.py



def test_insert_document():
    """Test if a document can be inserted into the database."""
    client = MongoClient('mongodb+srv://<username>:<password>@cluster.mongodb.net/test?retryWrites=true&w=majority')
    db = client['test_db']
    test_collection = db['test_collection']
    test_doc = {"name": "Test Product", "price": 100}

    # Insert the document
    result = test_collection.insert_one(test_doc)
    assert result.acknowledged, "Document insertion failed."

    # Query the document
    queried_doc = test_collection.find_one({"name": "Test Product"})
    assert queried_doc is not None, "Document not found in the database."

    def test_mongo_connection():
    """Test if MongoDB connection is active using ping."""
    try:
        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        client = MongoClient(f'mongodb+srv://{username}:{password}@cluster.mongodb.net/test?retryWrites=true&w=majority')
        client.admin.command('ping')  # Ping the MongoDB server
        assert True
    except Exception:
        assert False, "MongoDB connection failed."