# LuckyCode AI Assistant (Gemini Version)
### 🔗 Live Demo  
👉 **Try the app here:**  
[https://huggingface.co/spaces/Laxman-Sannu/LuckyCode-Gemini-Assistant](https://huggingface.co/spaces/Laxman-Sannu/LuckyCode-Gemini-Assistant)

LuckyCode is an AI-powered coding assistant built using **Google Gemini** and **Gradio**.  
It helps with debugging, code generation, explanations, and learning programming concepts — all through a simple web interface.

This version is optimized for **HuggingFace Spaces**, **Render**, and **local deployment**.

---

## 🚀 Features

- Powered by **Gemini 2.0 Flash**
- Accurate code reasoning
- Explains and debugs code in simple language
- Clean Gradio UI
- Supports multi-language coding (Python, Java, C++, JS, etc.)
- Uses API-based inference (no local GPU needed)

---

## 🛠️ Local Setup

### 1. Install dependencies

pip install -r requirements.txt

### 2. Add your Gemini API Key

Get it from:

https://aistudio.google.com/app/apikey

Set it locally:

export GEMINI_API_KEY="your_key_here"

shell
Copy code

### 3. Run the app

python app.py

yaml
Copy code

Open the local link in your browser.

---

## 🌐 Deploy to HuggingFace Spaces

1. Create a new Space → Choose **Gradio SDK**
2. Upload:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Go to **Settings → Secrets**
4. Add:
   - Name: `GEMINI_API_KEY`
   - Value: your API key
5. Space will rebuild automatically.

Done — your LuckyCode Assistant is live!

---

## 📁 Project Structure

LuckyCode-Gemini-Assistant/
│── app.py
│── requirements.txt
│── README.md
└── .gitignore

---

## 👤 Author

Created by **Laxman Sannu Gouda**  
LuckyCode – Your personal AI coding partner.

⭐ If you like this project, please star it on GitHub!
