# 🩺 Medical Abbreviation Expansion in Handwritten Text

Automatically identify and expand handwritten medical abbreviations like `b.i.d.` (twice daily), `p.o.` (by mouth), and more using OCR and a domain-specific lexicon.

---

## 📸 Overview

Doctors and healthcare professionals often use handwritten abbreviations in prescriptions and patient notes. These abbreviations may be hard to understand, especially for patients. This app extracts handwritten text and expands medical abbreviations into their full meanings using OCR and a custom dictionary.

---

## 🚀 Live Demo

Try it live (mobile-friendly) 👉 [Hugging Face Space](https://huggingface.co/spaces/YOUR_USERNAME/medical-abbreviation-expander)

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

## 📦 Installation (for local testing)

```bash
pip install gradio easyocr numpy pillow


---

📂 File Structure

File	Description

app.py	Main Gradio application
abbreviations.json	Dictionary of medical abbreviations
requirements.txt	Python dependencies
README.md	Project documentation (this file)



---

✨ Example

Input (Handwritten Image):

Take 1 tab b.i.d. p.o. after meals

Extracted Text:

Take 1 tab b.i.d. p.o. after meals

Expanded Output:

Take 1 tab twice daily by mouth after meals


---

✅ Supported Abbreviations

Here are a few supported examples (from abbreviations.json):

Abbreviation	Full Form

b.i.d.	twice daily
t.i.d.	three times daily
p.o.	by mouth
i.v.	intravenous
a.c.	before meals
p.c.	after meals
n.p.o.	nothing by mouth
q.d.	every day
p.r.n.	as needed


You can add more to the dictionary!


---

💡 Features

📸 Supports handwritten input (not just typed)

🧼 Cleans unwanted text like timestamps and labels

📱 100% mobile-friendly

🔍 Customizable dictionary



---

📌 Future Ideas

PDF export

More advanced text cleanup

Abbreviation confidence levels

Camera capture integration



---

🧾 License

This project is licensed under the MIT License.


---

🙋 Author

Karthikeyan Rayana
Capstone Project • 2025 
