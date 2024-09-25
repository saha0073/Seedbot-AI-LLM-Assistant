from langchain.tools.retriever import create_retriever_tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_pinecone import PineconeVectorStore
from langchain.tools import tool
from prompts import TOOLS_VERSION_ONE


class Tools:
    @staticmethod
    def setup_tools():
        retriever_tool_web_search = create_retriever_tool(
            GetRetriever("seedworld-whitepaper-rag"),  #
            "seedworld-whitepaper-search",
            TOOLS_VERSION_ONE,
        )

        tools = [retriever_tool_web_search]
        return tools
    
def GetRetriever(index_name):
    embeddings=OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    retriever = vectorstore.as_retriever()
    return retriever


