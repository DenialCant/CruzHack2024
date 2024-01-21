# Texty Bear - Flask Application

Welcome to **Texty Bear** Flask application!

Life is tough and sometimes you don't have time to watch full lectures. Texty Bear allows you to still learn that information in a fraction of a time.

By submitting a YouTube lecture URL, Texty Bear will automatically look for key points within the lecture and create notes just for you!

## Installation
1. **Create Virtual Environment:**

Run the following command to create a virtual environment:
```bash
cd path/to/your/project
```

Create a virtual environment named `venv`:
```bash
python -m venv venv
```

2. **Activate the Virtual Environment:**

On Linux or macOS:
```bash
source venv/bin/activate
```
On Windows (Command Prompt):
```bash
venv\Scripts\activate
```
On Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

3. **Install Dependencies:**

While the virtual environment is activated, install the required dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

Run the Flask Application:
```bash
python app.py
```
This will start your Flask application. Visit `http://127.0.0.1:5000/` in your browser to access the app.