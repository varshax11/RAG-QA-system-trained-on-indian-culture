# RAG System for Indian Culture Data

This repository contains a Retrieval-Augmented Generation (RAG) system for answering questions related to Indian culture. The project consists of two main components:

1. **Scraping Script**: A script to scrape Wikipedia or other websites to collect Indian culture-related text.
2. **RAG System**: A system that stores and retrieves Indian culture data from a vector database and generates responses using an LLM.
3. **Indian Culture Folder**: A pre-scraped dataset containing Indian culture texts, which can be used directly without scraping.

## Features
- Scrape Wikipedia or other sources for Indian culture data.
- Store extracted text in the `indian_culture` folder.
- Use ChromaDB for document retrieval.
- Process and chunk text for efficient storage and querying.
- Generate responses using Mistral-7B-Instruct-v0.1.

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### 1. Using the Pre-Scraped Data (No Scraping Required)
If you don’t want to scrape data, the `indian_culture` folder is already provided. The RAG system will use the text files inside this folder for retrieval.

Run the RAG system:
```bash
python rag_system.py
```

### 2. Scraping New Data
If you want to update or add more data, use the scraping script:
```bash
python scrape_wikipedia.py
```
This will fetch new text and store it in the `indian_culture` folder.

Then, run the RAG system as mentioned above.

## Folder Structure
```
📂 indian_culture_rag
 ├── 📂 indian_culture       # Pre-scraped text files on Indian culture
 ├── scrape_wikipedia.py     # Script to scrape Wikipedia or other websites
 ├── rag_system.py           # Main RAG system
 ├── requirements.txt        # Required dependencies
 ├── README.md               # This file
```

## Example Query
After running the RAG system, you can ask questions such as:
```
tell me about diwali
```
The system will retrieve relevant information and generate a response.

## License
This project is open-source. Feel free to contribute!
