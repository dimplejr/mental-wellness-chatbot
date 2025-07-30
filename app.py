import streamlit as st

st.title("Daily Wellness Check-in Chatbot")

with st.form("wellness_checkin"):
    st.subheader("Daily Check-in")
    
    mood = st.selectbox("How are you feeling today?", ["Happy","Sad","Anxious","Tired","Okay"])
    sleep = st.slider("How was your sleep last night? (0=Poor, 10=Great)", 0, 10, 5)
    energy = st.slider("Your energy Level today?(1=Low, 5=High)", 1, 5, 3)
    thoughts = st.text_area("Any thoughts you'd like to share", placeholder ="Type here ..")
    
    submit = st.form_submit_button("Submit")

if submit:
    st.success("Check-in submitted! Here's a quick summary:")
    st.write(f"**Mood:** {mood}")
    st.write(f"**Sleep Quality:** {sleep}/10")
    st.write(f"**Energy Level:** {energy}/10")
    st.write(f"**Notes:** {thoughts if thoughts else 'No additional thoughts'}")