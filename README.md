# SNS Automations – Caption Generator

This project generates social media captions automatically using a **template** and a **CSV file** of data.  
It’s useful for events, speaker lineups, or any repeated posts that share the same structure.

---

## 🚀 Features
- Fill in speaker name, title, company, and topic dynamically.
- Keep your captions consistent with a single template.
- Output to plain text (`captions.txt`) for easy copy-paste.
- Easily extendable to CSV output for scheduling tools.

---

## 📂 Project Structure
sns-automations/
├── generate_captions.py # Main script
├── template.txt # Caption template with placeholders
├── data.csv # Input data (speakers/topics)
└── captions.txt # Generated output (created after running)

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/chrisanne-cell/sns-automations.git
cd sns-automations

2. Create a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
# .\venv\Scripts\activate  # On Windows

3. Install dependencies

pip install -r requirements.txt

If you don’t have a requirements.txt, install manually:

pip install jinja2 python-dateutil

▶️ Usage
1. Edit the template
Open template.txt and customize your caption format. Example:

We're excited to have {{ speaker_name }}, {{ speaker_title }} of {{ speaker_company }},
join us for the Tech for Impact Summit 2025! 

Join {{ speaker_name }} in this session: {{ topic }}

📅 October 7 (Tue) at Toranomon Hills Forum, Tokyo
🎟️ Join the conversation: https://tech4impactsummit.com/tickets
2. Add your data
Edit data.csv with your speaker details. Example:

speaker_name,speaker_title,speaker_company,topic
Audrey Tang,Digital Minister,Taiwan,"Democracy & Digital Innovation"
Ken Shibusawa,CEO,Shibusawa & Co.,"Sustainability in Capitalism"
Kathy Matsui,General Partner,Mizuho Capital,"Womenomics & Future Growth"

3. Run the script
python generate_captions.py

4. Get the results
A new file captions.txt will appear with one caption per speaker.

✅ Example Output
We're excited to have Audrey Tang, Digital Minister of Taiwan, join us for the Tech for Impact Summit 2025! 

Join Audrey Tang in this session: Democracy & Digital Innovation

📅 October 7 (Tue) at Toranomon Hills Forum, Tokyo
🎟️ Join the conversation: https://tech4impactsummit.com/tickets
---
We're excited to have Ken Shibusawa, CEO of Shibusawa & Co., join us for the Tech for Impact Summit 2025! 

Join Ken Shibusawa in this session: Sustainability in Capitalism

📅 October 7 (Tue) at Toranomon Hills Forum, Tokyo
🎟️ Join the conversation: https://tech4impactsummit.com/tickets

👥 Contributing
Fork this repo

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-name)

Open a Pull Request

📄 License
MIT License — free to use and modify.