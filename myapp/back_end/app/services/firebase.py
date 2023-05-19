import firebase_admin
from firebase_admin import credentials, storage

firebaseConfig = {
  apiKey: "AIzaSyA6vzxLSXWfkulEvs7W8X5QDQ7gOmRK0vI",
  authDomain: "sf4-datalogger.firebaseapp.com",
  projectId: "sf4-datalogger",
  storageBucket: "sf4-datalogger.appspot.com",
  messagingSenderId: "321884813520",
  appId: "1:321884813520:web:16933dadbf5f68211bc6d5",
  measurementId: "G-48BYQ43B49"
};

cred = credentials.Certificate(firebaseConfig.apiKey)
firebase_admin.initialize_app(cred, {
    'storageBucket': firebaseConfig.storageBucket
})

bucket = storage.bucket()

def upload_file(filename):
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    return blob.public_url
