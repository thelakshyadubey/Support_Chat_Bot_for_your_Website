from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone as PineconeStore
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.document_loaders.sitemap import SitemapLoader
from pinecone import Pinecone as PineconeClient

def get_website_data(sitemap_url):
    loader = SitemapLoader(sitemap_url)
    docs = loader.load()
    return docs

def split_data(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_documents(docs)

def create_embeddings():
    return SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def push_to_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings, docs):
    pc = PineconeClient(api_key=pinecone_apikey, environment=pinecone_environment)
    if pinecone_index_name not in [i['name'] for i in pc.list_indexes()]:
        pc.create_index(name=pinecone_index_name, dimension=384, metric="cosine")
    index = PineconeStore.from_documents(docs, embeddings, index_name=pinecone_index_name)
    return index

def pull_from_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings):
    PineconeClient(api_key=pinecone_apikey, environment=pinecone_environment)
    return PineconeStore.from_existing_index(index_name=pinecone_index_name, embedding=embeddings)

def get_similar_docs(index, query, k=2):
    return index.similarity_search(query, k=k)
