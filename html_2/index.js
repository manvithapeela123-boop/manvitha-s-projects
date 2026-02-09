import { initializeApp } from "https://www.gstatic.com/firebasejs/11.7.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.7.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyAFpp0EGeZY8BV0Xzkquh6u34xJXN7Wr0k",
  authDomain: "my-amazing-project-3d59c.firebaseapp.com",
  projectId: "my-amazing-project-3d59c",
  storageBucket: "my-amazing-project-3d59c.appspot.com",
  messagingSenderId: "1072030425856",
  appId: "1:1072030425856:web:3014b81021d32b28c609e5",
  measurementId: "G-495G7LNEFG"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Check if user is already logged in and redirect
onAuthStateChanged(auth, (user) => {
  if (user) {
    window.location.href = "index.html";
  }
});

document.getElementById("login-form").addEventListener("submit", (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const errorMessage = document.getElementById("error-message");

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      // Successful login — redirect to home page
      window.location.href = "index.html";
    })
    .catch((error) => {
      errorMessage.textContent = "Login failed: " + error.message;
    });
});
