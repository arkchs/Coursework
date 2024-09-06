import json
class CloudStorageSim:
    def __init__(self, filename):
        self.filename = filename
    def upload(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)
    def download(self):
        with open(self.filename, 'r') as file:
            return json.load(file)
data = {"name": "Alice", "age": 30, "city": "Wonderland"}
cloud_storage = CloudStorageSim('data.json')
cloud_storage.upload(data)
loaded_data = cloud_storage.download()
print(f"Loaded data: {loaded_data}")
