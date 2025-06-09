import streamlit as st
from utils import *
import os
from dotenv import load_dotenv

# Inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Get API keys and constants from .env
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

st.title("🤖 AI Assistance For Website")

# Input for sitemap URL
st.markdown("### Enter Sitemap URL")
example_url = "https://www.coursera.org/sitemap~www~resources.xml"
default_url = st.text_input(
    "Enter a valid sitemap.xml URL",
    placeholder="e.g., https://www.coursera.org/sitemap~www~resources.xml",
    key="website_url"
)

st.caption(f"💡 Example: `{example_url}`")
if st.button("Use Example URL"):
    st.session_state['website_url'] = example_url

# Button to load and push data to Pinecone
if st.button("📤 Load Data to Pinecone"):
    if default_url:
        site_data = get_website_data(default_url)
        st.success("✅ Data pull successful.")

        chunks_data = split_data(site_data)
        st.success("✅ Data split successful.")

        embeddings = create_embeddings()
        st.success("✅ Embeddings initialized.")

        push_to_pinecone(PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX, embeddings, chunks_data)
        st.success("✅ Data pushed to Pinecone.")
    else:
        st.error("🚫 Please provide a valid sitemap URL.")

# Input prompt for querying
prompt = st.text_input('🧠 Ask me something about the website:', key="prompt")
document_count = st.slider('🔗 No. of links to return', 0, 5, 2, step=1)

if st.button("🔍 Search"):
    if prompt and default_url:
        embeddings = create_embeddings()
        index = pull_from_pinecone(PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX, embeddings)

        relavant_docs = get_similar_docs(index, prompt, document_count)
        st.success("✅ Here are the results:")

        for idx, document in enumerate(relavant_docs, 1):
            st.markdown(f"### 👉 Result {idx}")
            st.write("**Info**:", document.page_content)
            st.write("**Link**:", document.metadata['source'])
    else:
        st.error("❗ Please provide both a sitemap URL and a prompt.")

local_css("style.css")