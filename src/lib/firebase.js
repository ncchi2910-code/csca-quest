// Firebase: Google sign-in + Firestore cloud save for cross-device progress sync.
// All config below is PUBLIC by design (it ships in the browser bundle); access is
// protected by Firestore security rules, not by hiding these keys.
// The app works fully offline/localStorage-only when config is absent — sync is opt-in.
import { initializeApp } from "firebase/app";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged
} from "firebase/auth";
import { getFirestore, doc, getDoc, setDoc } from "firebase/firestore";

const config = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID
};

// Cloud sync is only active once the Firebase project keys are configured.
export const cloudEnabled = Boolean(config.apiKey && config.projectId);

let auth = null;
let db = null;
if (cloudEnabled) {
  const app = initializeApp(config);
  auth = getAuth(app);
  db = getFirestore(app);
}

const provider = cloudEnabled ? new GoogleAuthProvider() : null;

// Subscribe to auth changes. Returns an unsubscribe fn (no-op if cloud disabled).
export function watchAuth(cb) {
  if (!auth) return () => {};
  return onAuthStateChanged(auth, cb);
}

export async function signInWithGoogle() {
  if (!auth) return;
  await signInWithPopup(auth, provider);
}

export async function signOutUser() {
  if (!auth) return;
  await signOut(auth);
}

// Read this user's saved progress from Firestore (null if none yet).
export async function pullProgress(uid) {
  if (!db) return null;
  const snap = await getDoc(doc(db, "progress", uid));
  return snap.exists() ? snap.data() : null;
}

// Write this user's progress to Firestore.
export async function pushProgress(uid, data) {
  if (!db) return;
  await setDoc(doc(db, "progress", uid), data);
}
