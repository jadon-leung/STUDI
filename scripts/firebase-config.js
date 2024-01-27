import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js';
import { getAuth, createUserWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js';
import { getDatabase } from 'https://www.gstatic.com/firebasejs/10.7.2/firebase-database.js';



const firebaseConfig = {
    apiKey: "AIzaSyAQ1j9ImVzvO7w_V3jc0KznSV52c4ssJ5g",
    authDomain: "studi-31486.firebaseapp.com",
    databaseURL: "https://studi-31486-default-rtdb.firebaseio.com",
    projectId: "studi-31486",
    storageBucket: "studi-31486.appspot.com",
    messagingSenderId: "919376410608",
    appId: "1:919376410608:web:40c513b7bdee38fcb24f35",
    measurementId: "G-JGVEH7P7CP"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const database = getDatabase(app);

export { auth, createUserWithEmailAndPassword, database};
