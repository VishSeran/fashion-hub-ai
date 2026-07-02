from typing import Optional
import requests
from configuration.config import IMAGE_MODEL
from transformers import CLIPModel, CLIPProcessor
import torch
import io
from PIL import Image

from configuration.logger import get_logger

logger = get_logger("image-processor")

class Image_Model:
    
    def __init__(self, model_name=IMAGE_MODEL):
        
        try:
            
            if not model_name:
                raise ValueError("Model name must not be empty")
            
            self.device = torch.device(
                "cuda" if torch.cuda.is_available() else "cpu")
            
            self.model = CLIPModel.from_pretrained(
                model_name).to(self.device)
            
            self.processor = CLIPProcessor.from_pretrained(model_name)
            
            self.model.eval()
            
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
    
        except Exception as e:
            logger.error(f"Error in model initialization: {e}")
            raise
            
    def encode_image(self, image_path:Optional[str],
                     image_url:Optional[str]):
        
        try:
            if image_url:
                image_loaded = requests.get(image_url, 
                                     timeout=30, 
                                     stream=True).content
                
                image = Image.open(io.BytesIO(image_loaded)).convert("RGB")
                
            
            if image_path:
                image = Image.open(image_path).convert("RGB")
            
            if image is None:
                raise ValueError("Error in image feching")
            
            
            
                                 
            
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
    
        except Exception as e:
            logger.error(f"Error in encoding image: {e}")
            raise
        
        