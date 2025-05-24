import streamlit as st
import openai

st.set_page_config(page_title="Proposal Compliance Agent", layout="wide")

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Proposal Compliance & Review Agent")

st.markdown("Paste your full proposal text below:")

proposal = st.text_area("Proposal Content", height=400)

if st.button("Run Compliance & Review Check"):
    with st.spinner("Analyzing..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a NASA compliance checker and reviewer. Confirm section presence and simulate feedback."},
                {"role": "user", "content": proposal}
            ]
        )
        result = response.choices[0].message.content
        st.markdown("### ✅ Results")
        st.markdown(result)
