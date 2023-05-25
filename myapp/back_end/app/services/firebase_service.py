from firebase_admin import storage, firestore, initialize_app, credentials, _apps
import uuid

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
    
    def save_to_firestore(self, collection_name, document_name, data):
        unique_id = str(uuid.uuid4())
        doc_ref = self.db.collection(collection_name).document(unique_id)
        data["id"] = unique_id
        doc_ref.set(data)
        return unique_id

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
