import faiss
from configuration.logger import get_logger
from langchain_community.document_loaders import WebBaseLoader

logger = get_logger("faiss-index")



class FaissIndex:
    
    def __init__(self, dim=512):
        self.index = faiss.IndexFlatIP(dim)
        
    def add(self, embeddings):
        
        try:
            if not embeddings:
                raise ValueError("image embeddings are empty or none")
            
            self.index.add(embeddings)
            
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
    
        except Exception as e:
            logger.error(f"Error in encoding image: {e}")
            raise
        
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