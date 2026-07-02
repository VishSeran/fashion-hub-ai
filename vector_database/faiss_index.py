import faiss

class FaissIndex:
    
    def __init__(self, dim=512):
        self.index = faiss.IndexFlatIP(dim)
        
    def add(self, embeddings):
         
        