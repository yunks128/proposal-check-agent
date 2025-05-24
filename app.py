import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="Proposal Compliance Agent", layout="wide")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# App title and description
st.title("Proposal Compliance & Review Agent")
st.markdown("Paste your full proposal text below:")

# Input area
proposal = st.text_area("Proposal Content", height=400)

# Analysis button
if st.button("Run Compliance & Review Check"):
    if proposal.strip():
        with st.spinner("Analyzing..."):
            try:
                # Updated API call using the new OpenAI client
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are a NASA compliance checker and reviewer. Analyze the proposal for required sections, formatting compliance, and provide constructive feedback on content quality, technical feasibility, and adherence to NASA standards."
                        },
                        {
                            "role": "user", 
                            "content": f"Please review this proposal for compliance and quality:\n\n{proposal}"
                        }
                    ],
                    max_tokens=2000,
                    temperature=0.3
                )
                
                result = response.choices[0].message.content
                
                # Display results
                st.markdown("### ✅ Compliance & Review Results")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"Error analyzing proposal: {str(e)}")
                st.info("Please check your OpenAI API key and try again.")
    else:
        st.warning("Please enter some proposal content before running the analysis.")
