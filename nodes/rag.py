from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


DB_PATH = "vectorstore"

def create_vectorstore():
    documents = []
    pdfs = Path("documents").glob("*.pdf")

    for pdf in pdfs:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150

    )

    chunks = splitter.split_documents(documents)
    Chroma.from_documents(
        chunks,
        embedding,
        persist_directory=DB_PATH

    )



def retrieve(query):
    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    retriever = db.as_retriever(
        search_kwargs={"k":4}
    )

    docs = retriever.invoke(query)
    return "\n\n".join(
        doc.page_content
        for doc in docs

    )
print("Vector Store Created Successfully")