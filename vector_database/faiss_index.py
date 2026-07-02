import faiss

from configuration.logger import get_logger

logger = get_logger("faiss-index")
class FaissIndex:
    
    def __init__(self, dim=512):
        self.index = faiss.IndexFlatIP(dim)
        
    def add(self, embeddings):
        self.index.add(embeddings)
        
    def search(self, query_embedding, k=5):
        
        try:
            distance, indices = self.index.search(query_embedding,k=k)
            logger.info("Distance and Indices are created")
            return distance, indices
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
    
        except Exception as e:
            logger.error(f"Error in faiss index search for query embeddings: {e}")
            raise