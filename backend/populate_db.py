import chromadb

# Step 1: Create a client
client = chromadb.Client()

# Step 2: Create or get a collection
collection = client.get_or_create_collection(name="career_data")

# Step 3: Add documents
collection.add(
    documents=[
        "Software Engineer: Requires skills in Python, Data Structures, Algorithms, System Design.",
        "Data Scientist: Requires Python, Statistics, Machine Learning, Data Visualization.",
        "Cloud Architect: Requires Cloud Platforms (AWS/Azure/GCP), Networking, Security, DevOps.",
        "Database adminstrator:Reqiures SQL"
    ],
    ids=["doc1", "doc2", "doc3","doc4"]
)

print("Database populated!")
