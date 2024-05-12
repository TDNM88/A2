# llm_evaluation.py
from transformers import model_path, VQQ2VecProcessor, VQQ2VecForImageDescription

MODEL_NAME = "your_vq_model"
TOKENIZER = VQQ2VecProcessor.from_pretrained(MODEL_NAME)
MODEL = VQQ2VecForImageDescription.from_pretrained(MODEL_NAME)

def embed_image(image_path):
    inputs = TOKENIZER(image_path, return_tensors="pt", max_length=16)
    return MODEL(**inputs).pooler_output