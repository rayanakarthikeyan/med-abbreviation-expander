# 🩺 Medical Abbreviation Expansion in Handwritten Text

Automatically identify and expand handwritten medical abbreviations like `b.i.d.` (twice daily), `p.o.` (by mouth), and more using OCR and a domain-specific lexicon.

---

## 📸 Overview

Doctors and healthcare professionals often use handwritten abbreviations in prescriptions and patient notes. These abbreviations may be hard to understand, especially for patients. This app extracts handwritten text and expands medical abbreviations into their full meanings using OCR and a custom dictionary.

---

## 🚀 Live Demo

Try it live (mobile-friendly) 👉 [Hugging Face Space](https://huggingface.co/spaces/karthikeyanr05/med-abbreviation-expander)

> 📱 Upload a handwritten note or prescription photo — get instant expanded abbreviations!

---

## 🛠️ Tech Stack

- **Python** – main programming language  
- **Gradio** – simple, interactive web UI  
- **EasyOCR** – Optical Character Recognition for handwriting  
- **Hugging Face Spaces** – free hosting & deployment  
- **Custom Lexicon** – dictionary of common medical abbreviations

---

## 🧠 How It Works

1. Upload a photo of handwritten text.
2. OCR extracts the text.
3. The app detects abbreviations using a medical dictionary.
4. It replaces abbreviations with full forms and ignores unrelated noise like timestamps or titles.

---
