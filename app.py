import pyrebase

config = {
    apiKey: "AIzaSyAQ1j9ImVzvO7w_V3jc0KznSV52c4ssJ5g",
  authDomain: "studi-31486.firebaseapp.com",
  databaseURL: "https://studi-31486-default-rtdb.firebaseio.com",
  projectId: "studi-31486",
  storageBucket: "studi-31486.appspot.com",
  messagingSenderId: "919376410608",
  appId: "1:919376410608:web:40c513b7bdee38fcb24f35",
  measurementId: "G-JGVEH7P7CP"
}

app = pyrebase.initialize_app(config)
database = app.database()

