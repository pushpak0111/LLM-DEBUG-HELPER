import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Streamlit page configuration
st.set_page_config(page_title="Python Debug Helper", page_icon="🐍")
st.title("🐍 LLM-Powered Debug Helper")
st.markdown("Explain Python errors using Gemini and get suggestions for fixes.")

# Configure the Gemini API client using the API key from environment variables
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    st.error(f"❌ Gemini API configuration error: {e}")
    st.stop()  # Stop the app if the API key is not configured

# Initialize session state for the input if it doesn't exist
if 'error_input' not in st.session_state:
    st.session_state.error_input = ""
if 'explanation' not in st.session_state:
    st.session_state.explanation = ""

# Text input for the error, tied to session state
st.session_state.error_input = st.text_area(
    "🔍 Paste your Python error or traceback here:",
    value=st.session_state.error_input,
    height=200
)

# Button to trigger the explanation
if st.button("💡 Explain Error"):
    if not st.session_state.error_input.strip():
        st.warning("Please enter a Python error first.")
    else:
        with st.spinner("Contacting Gemini..."):
            try:
                # Create the prompt for the Gemini model
                prompt = f"""You are a Python expert. Explain the following error and how to fix it with a simple code example.

Error:
```python
{st.session_state.error_input}
```"""

                # Use a valid model name
                model = genai.GenerativeModel('gemini-2.5-pro')

                # Generate explanation
                response = model.generate_content(prompt)
                
                # Update the session state with the new explanation
                st.session_state.explanation = response.text

            except Exception as e:
                # Display an error message if the API call fails
                st.error(f"❌ Gemini API error: {e}")

# Display the explanation if it's available in the session state
if st.session_state.explanation:
    st.success("✅ Explanation:")
    st.markdown(st.session_state.explanation)
