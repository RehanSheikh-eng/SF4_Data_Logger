from firebase_admin import storage, firestore, initialize_app, credentials
import uuid

class FirebaseService:
    def __init__(self):
        self.cred = credentials.Certificate("C:/Users/relic/Documents/School/Engineering_Cam/Part IIA/SF4/SF4_Data_Logger/myapp/back_end/sf4-datalogger-firebase-adminsdk-fk860-bfaeafc479.json")
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
        doc_ref.set(data)
        return unique_id

