from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader

# from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter

# splitter = CharacterTextSplitter(
#     separator="",
#     chunk_size=10,
#     chunk_overlap=1
# )

splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)
data = PyPDFLoader(r"C:\Users\anshu varma\Desktop\GenAi\RAGProject\document loaders\GRU.pdf")
docs = data.load()
chunks = splitter.split_documents(docs)
print(chunks[0].page_content)