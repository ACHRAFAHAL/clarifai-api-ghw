import streamlit as st
from Clarifai_lib import ClarifaiHelper

# Set up page configuration
st.set_page_config(
    page_title="AI Models Dashboard",
    page_icon="🤖"
)

# Initialize the helper
@st.cache_resource
def get_clarifai():
    if 'CLARIFAI_API_KEY' not in st.secrets:
        st.error('CLARIFAI_API_KEY not found in secrets!')
        st.stop()
    return ClarifaiHelper(api_key=st.secrets['CLARIFAI_API_KEY'])

clarifai = get_clarifai()

# Main interface
st.title("🤖 Multi-Model AI Chat")
st.write("Ask a question and compare responses from different AI models!")

# User input
question = st.text_area("Enter your question:", height=100)

# Model selection
model = st.radio(
    "Choose an AI model:",
    ["ChatGPT", "DeepSeek", "Gemini"],
    horizontal=True
)

# Temperature slider
temperature = st.slider(
    "creativity level:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

if st.button("Get Response"):
    if question:
        with st.spinner(f"Getting response from {model}..."):
            response = clarifai.get_response(model, question, temperature)
            st.success("Response received!")
            st.write(response)
    else:
        st.warning("Please enter a question first!")