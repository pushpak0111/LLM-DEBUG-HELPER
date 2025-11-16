# 🐍 LLM-Powered Debug Helper

An AI-powered tool that explains Python errors and suggests fixes interactively using **Google Gemini 2.5 Flash**.  
Built with a clean Streamlit interface and designed to make debugging faster, easier, and beginner-friendly.

---
## 📸 Screenshot
<img width="1629" height="907" alt="image" src="https://github.com/user-attachments/assets/1c416d01-5460-4fe8-a78e-e2e72e6698a3" />
<img width="1597" height="861" alt="image" src="https://github.com/user-attachments/assets/1b63ff54-9b0f-4e66-802f-9f6e224294da" />


## 🚀 Features

- 📝 Paste any Python error or traceback  
- 🤖 Get clear explanations written in simple language  
- 🔧 Receive suggested fixes + example code  
- ⚡ Powered by **Gemini 2.5 Flash** for fast responses  
- 🎨 Modern and clean Streamlit UI  
- 🔐 Secure API handling using `.env`

---

## 📂 Project Structure

```
LLM-DEBUG-HELPER/
│
├── assets/
│   └── screenshot.png        # App screenshot (optional)
│
├── debug_helper.py           # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .env                      

```
---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
bash
git clone https://github.com/pushpak0111/LLM-DEBUG-HELPER.git
cd LLM-DEBUG-HELPER

### 2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your Gemini API key
GEMINI_API_KEY=your_api_key_here

### ▶️ Running the App
Start the Streamlit app:
streamlit run debug_helper.py

Your browser will open with the LLM Debug Helper interface.

🧠 How it Works

- You paste a Python error or traceback

- The app sends it to Gemini 2.5 Flash

- The LLM:

-- Reads the traceback

-- Explains the error in simple words

-- Suggests clear fixes

-- Generates example corrected code

- The explanation is displayed beautifully in the UI


## 📦 Requirements 
Listed in requirements.txt:
streamlit
google-generativeai
python-dotenv



