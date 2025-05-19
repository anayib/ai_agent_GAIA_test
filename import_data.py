import os
import json
import numpy as np
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from supabase.client import create_client
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

def main():
    print("Starting data import process...")
    
    # 1. Configure embeddings model
    print("Initializing embeddings model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    # 2. Initialize Supabase client
    print("Connecting to Supabase...")
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
    
    if not supabase_url or not supabase_key:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in .env file")
    
    supabase = create_client(supabase_url, supabase_key)
    
    # 3. Read metadata.jsonl file
    print("Reading metadata.jsonl file...")
    questions = []
    with open("metadata.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            try:
                question = json.loads(line.strip())
                questions.append(question)
            except json.JSONDecodeError as e:
                print(f"Error parsing line: {line[:50]}... - {e}")
    
    print(f"Found {len(questions)} questions to process")
    
    # 4. Process each question and upload to Supabase
    print("Generating embeddings and uploading to Supabase...")
    batch_size = 10  # Adjust based on your needs
    
    for i in tqdm(range(0, len(questions), batch_size)):
        batch = questions[i:i+batch_size]
        batch_data = []
        
        for question in batch:
            # Create the content that will be retrieved
            content = f"Question: {question['Question']}\nFinal answer: {question.get('Final answer', '?')}"
            
            # Generate embedding for the question
            embedding = embeddings.embed_query(question["Question"])
            
            # Prepare data for insertion
            batch_data.append({
                "content": content,
                "metadata": question,
                "embedding": embedding
            })
        
        try:
            # Insert batch into Supabase
            result = supabase.table("documents").insert(batch_data).execute()
            # Check for errors in response
            if hasattr(result, 'error') and result.error:
                print(f"Error inserting batch: {result.error}")
        except Exception as e:
            print(f"Exception during batch upload: {e}")
    
    print("Data import completed successfully!")

if __name__ == "__main__":
    main()