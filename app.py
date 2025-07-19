import gradio as gr
import easyocr
import numpy as np
from PIL import Image
import re
import json

# Load medical abbreviations from a JSON file
with open("abbreviations.json", "r") as f:
    abbreviations = json.load(f)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

def expand_abbreviations(text):
    # Fix spaced-out abbreviations like "B. I. D." → "B.I.D."
    text = re.sub(r'\b([A-Za-z])\.?\s+([A-Za-z])\.?\s+([A-Za-z])\.?\b', r'\1.\2.\3.', text)

    words = text.split()
    expanded_words = []

    for word in words:
        original = word
        clean = re.sub(r'[^\w]', '', word.lower())  # Remove punctuation

        candidates = [
            clean,
            clean.replace(".", ""),
            clean.lower()
        ]

        match = None
        for candidate in candidates:
            if candidate in abbreviations:
                match = abbreviations[candidate]
                break

        if match:
            expanded_words.append(match)

    return ' '.join(expanded_words) if expanded_words else "No medical abbreviations found."

def process_image(image):
    img_array = np.array(image)
    results = reader.readtext(img_array, detail=0)
    extracted_text = ' '.join(results)

    if not extracted_text.strip():
        return "❌ No text detected.", ""

    expanded_text = expand_abbreviations(extracted_text)
    return extracted_text, expanded_text

# Gradio UI
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="📷 Upload Handwritten Note"),
    outputs=[
        gr.Textbox(label="📝 Extracted Text"),
        gr.Textbox(label="🧠 Expanded Abbreviations")
    ],
    title="🩺 Medical Abbreviation Expander",
    description="Upload a handwritten note containing medical abbreviations (e.g., 'b.i.d.', 'p.o.') and get full-form meanings instantly."
)

iface.launch()
