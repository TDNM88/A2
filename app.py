# app.py
from transformers import pipeline
import random
import os

from theme_generator import generate_random_theme
from canvas_drawing import create_canvas, user_drawing, save_canvas
from llm_evaluation import embed_image
from classifier import initialize_model, predict_scores

# Initialize LLM-based theme generator
theme_generator = pipeline("text-generation", model=generate_random_theme, tokenizer=TOKENIZER)

# Initialize classifier model
classifer_model = initialize_model()

# Load pre-trained models ( bạn cần tải các mô hình đã được đào tạo trước vào )

def get_theme():
    return theme_generator()["generated_text"]

def evaluate_drawing(image_path):
    # Convert image path to embedding
    embeds = embed_image(image_path)

    # Predict using classifier
    scores = predict_scores(classifer_model, embeds)

    return scores

def run_app():
    # Create canvas and get random theme
    canvas = create_canvas()
    random_theme = get_theme()
    print("Your theme is:", random_theme)

    # User drawing session
    user_drawing(canvas)

    # Save canvas drawing
    save_canvas(canvas)

    # Evaluate drawing
    scores = evaluate_drawing("drawn_picture.jpg")
    print("LLM Evaluation Scores:", scores)

if __name__ == "__main__":
    run_app()