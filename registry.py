import streamlit as st
from google.cloud import firestore

st.title('Restaurant Rescue Registry')
st.subheader('A list of records of restaurant rescue sessions')
st.write('________________________________________________________________________')

db = firestore.Client.from_service_account_json("firestore-key.json")
st.session_state.interactions = []

doc_ref = db.collection("reports")
for doc in doc_ref.stream():
    st.session_state.interactions.append({"id": doc.get("id"),
                                          "message": doc.get("message"),
                                          "response": doc.get("response"),})

st.session_state.interactions.reverse()
for interation in st.session_state.interactions:
    st.write("**Feedback form id:** ", interation["id"])
    st.write("**Message from customer to employee:** ", interation["message"])
    st.write("**Message from employee to customer:** ", interation["response"])
    st.write('________________________________________________________________________')