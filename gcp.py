from google.cloud import storage

# Create a Storage client
client = storage.Client()
print(client)
# List all the buckets
buckets = client.list_buckets()

# Print the name of each bucket
for bucket in buckets:
    print(bucket.name)
    print(bucket.name)
    print(bucket.name)