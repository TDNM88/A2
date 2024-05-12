# theme_generator.py
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

MODEL_NAME = "distilbert-base-uncased"
TOKENIZER = DistilBertTokenizerFast.from_pretrained(MODEL_NAME)
MODEL = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)

def generate_random_theme():
    input_text = "random topic: "
    max_length = 15
    output = TOKENIZER.encode(input_text, return_tensors="pt", max_length=max_length, truncation=True)
    random_topic = TOKENIZER.decode(MODEL(output)[0][0], skip_special_tokens=True)
    return random_topic