import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(name=collection_name)

def get_local_embedding(text):
    return embedding_model.encode(text).tolist()


def load_documents_from_directory(directory_path):
    print("==== Loading documents from directory ====")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(directory_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append({"id": filename, "text": file.read()})
    return documents

def split_text(text, chunk_size=1000, chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks


directory_path = "indian_culture"
documents = load_documents_from_directory(directory_path)
print(f"Loaded {len(documents)} documents")


chunked_documents = []
for doc in documents:
    chunks = split_text(doc["text"])
    print(f"Splitting {doc['id']} into {len(chunks)} chunks")
    for i, chunk in enumerate(chunks):
        chunk_id = f"{doc['id']}_chunk{i+1}"
        embedding = get_local_embedding(chunk)
        chunked_documents.append({"id": chunk_id, "text": chunk, "embedding": embedding})
        collection.upsert(ids=[chunk_id], documents=[chunk], embeddings=[embedding])
print("==== Documents stored in ChromaDB ====")

def query_documents(question, n_results=2):
    question_embedding = get_local_embedding(question)
    results = collection.query(query_embeddings=[question_embedding], n_results=n_results)
    print("===== Query Results from ChromaDB =====")
    print(results)
    relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
    if not relevant_chunks:
        print("⚠️ No relevant chunks found. Check embeddings and stored documents.")
    return relevant_chunks


model_name = "mistralai/Mistral-7B-Instruct-v0.1"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config, device_map="auto")
llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(question, relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    prompt = f"""You are an expert in Indian culture. Use the provided context to answer:

    Context:\n{context}\n
    Question: {question}
    Answer:"""
    response = llm(prompt, max_new_tokens=200)
    return response[0]["generated_text"] if response else "No response generated."


question = "Tell me about Diwali"
relevant_chunks = query_documents(question)
answer = generate_response(question, relevant_chunks)
print(answer)
