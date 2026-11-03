# Naive chunking logic using a hard token text splitter rule
def chunk_and_filter_document(raw_text, doc_id):
    # Split text greedily based on standard sentence markers
    raw_chunks = split_by_regex(raw_text, delimiter=r"\n\n|\. ")
    
    processed_embeddings_payload = []
    for index, chunk in enumerate(raw_chunks):
        # BUG: A rigid min-length parameter drops anything under 40 characters
        # intended to filter out trailing page numbers or whitespace fragments
        if len(chunk.strip()) < 40:
            continue 
            
        processed_embeddings_payload.append({
            "chunk_id": f"{doc_id}_ch_{index}",
            "text": chunk.strip()
        })
        
    return processed_embeddings_payload