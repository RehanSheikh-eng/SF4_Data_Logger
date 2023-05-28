import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';


const firebaseConfig = {
  apiKey: "AIzaSyA6vzxLSXWfkulEvs7W8X5QDQ7gOmRK0vI",
  authDomain: "sf4-datalogger.firebaseapp.com",
  projectId: "sf4-datalogger",
  storageBucket: "sf4-datalogger.appspot.com",
  messagingSenderId: "321884813520",
  appId: "1:321884813520:web:16933dadbf5f68211bc6d5",
  measurementId: "G-48BYQ43B49"
};


const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export default db;
