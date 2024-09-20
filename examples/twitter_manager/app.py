import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Lyzr Twitter Agent",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

# Initialize the LyzrAgent
client = AgentAPI(x_api_key=LYZR_API_KEY)

# Set up two columns for input and output areas
col1, col2 = st.columns([1, 1])  # Adjust the ratio to match the design in the image

with col1:
    st.markdown("## Lyzr Twitter Agent")

    # Input area for the query
    query = st.text_area("Enter Text Here", height=150)

    # Generate button
    if st.button("Generate"):
        if query.strip():
            with st.spinner("🕵🏼‍Researching About Your Topic..."):

                with st.spinner("⚙️Crafting And Posting...."):
                    response = client.chat_with_agent(
                        json_body=ChatRequest(
                            user_id="user@example.com",
                            agent_id=AGENT_ID,
                            message=query,
                            session_id="sdfw",
                        )
                    )
                    st.markdown("🤯Research Completed")
                    st.markdown("✅Crafting and Posting Is Completed")

                # Display the response in the second column
                with col2:
                    st.markdown("## Response:")
                    st.markdown(f"**Thoughts:**\n\n{response}")
        else:
            st.warning("Please provide Text")

# Optional footer
st.markdown("---")
st.markdown("Powered by Lyzr and OpenAI")
