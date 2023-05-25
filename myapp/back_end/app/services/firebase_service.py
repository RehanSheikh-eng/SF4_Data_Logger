from firebase_admin import storage, firestore, initialize_app, credentials, _apps

class FirebaseService:
    def __init__(self):
        self.cred = credentials.Certificate("C:/Users/relic/Documents/School/Engineering_Cam/Part IIA/SF4/SF4_Data_Logger/myapp/back_end/sf4-datalogger-firebase-adminsdk-fk860-d7a1a6c3c6.json")
        if not _apps:
            initialize_app(self.cred, {
                'storageBucket': 'sf4-datalogger.appspot.com',
            })
        self.db = firestore.client()
        self.bucket = storage.bucket()

    def upload_to_storage(self, filename, file_obj):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file_obj)
        # Make the blob publicly viewable
        blob.make_public()
        # Return the blob's public url
        return blob.public_url
    
    def save_to_firestore(self, collection_name, unique_id, data):
        doc_ref = self.db.collection(collection_name).document(unique_id)
        doc_ref.set(data)

    def get_all_from_collection(self, collection_name):
        docs = self.db.collection(collection_name).stream()
        result = []
        for doc in docs:
            result.append(doc.to_dict())
        return result
        
    def get_from_firestore(self, collection_name, document_id):
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
