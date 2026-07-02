from typing import Optional

from configuration.config import IMAGE_MODEL
from transformers import CLIPModel, CLIPProcessor
import torch


class Image_Model:
    
    def __init__(self, model_name=IMAGE_MODEL):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        
        self.model = CLIPModel.from_pretrained(
            model_name).to(self.device)
        
        self.processor = CLIPProcessor.from_pretrained(model_name)
        
        self.model.eval()
        
    def encode_image(self, image_path:Optional[str],
                     image_url:Optional[str]):
        
        