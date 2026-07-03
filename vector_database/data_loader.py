from langchain_community.document_loaders import WebBaseLoader

from configuration.logger import get_logger

logger = get_logger("data-loader")


class DatasetLoader:
    
    def __init__(self, url):
        
        try:
            if not url:
                raise ValueError ("URL of dataset must not be empty or none")
                
            self.data_loader = WebBaseLoader(url)
            self.data = self.data_loader.load()
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
        
        except Exception as e:
            logger.error(f"Error in URL dataset: {e}")
            raise