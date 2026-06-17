from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM


class RAGService:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.llm = OllamaLLM(
            model="llama3.2",
            base_url="http://host.docker.internal:11434"
        )

        self.vectorstore = None
        self.retriever = None

        self.load_vectorstore()

    def load_vectorstore(self):

        try:

            self.vectorstore = FAISS.load_local(
                "faiss_index",
                self.embeddings,
                allow_dangerous_deserialization=True
            )

            self.retriever = self.vectorstore.as_retriever(
                search_kwargs={"k": 5}
            )

            print("Vectorstore loaded")

        except Exception:

            print("No vectorstore found")

    def ingest_pdf(self, pdf_path):

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(docs)

        vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        vectorstore.save_local("faiss_index")

        # Refresh memory immediately
        self.load_vectorstore()

        return len(chunks)

    def ask(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

        return self.llm.invoke(prompt)