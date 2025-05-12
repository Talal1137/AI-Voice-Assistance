# 🗣️ Voice Appointment Bot using Twilio + Wit.ai + Flask

This is a simple voice bot that lets users call a number, speak their name, address, and appointment time — and it will automatically extract the details using **Wit.ai** and save them to a `.csv` file!

## 💡 What It Does

- Answers calls using Twilio
- Asks for the caller's name, address, and time
- Extracts the details using AI (Wit.ai)
- Saves the info into `appointments.csv`

---

## 🚀 Getting Started (For Beginners)

### ✅ Prerequisites

Before starting, install:

1. [Python](https://www.python.org/downloads/) (v3.8+)
2. [Ngrok](https://ngrok.com/download) (for creating public links)
3. [Git](https://git-scm.com/downloads) *(optional but recommended)*

You’ll also need:

- A [Twilio account](https://www.twilio.com/)
- A [Wit.ai account](https://wit.ai/) with a trained app

---

### 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Or simply Download ZIP from GitHub and extract it.

📁 Step 2: Install Dependencies
Open a terminal/command prompt in the project folder and run:
pip install flask twilio requests

🧠 Step 3: Set Your Wit.ai Token
Open app.py and find this line:
WIT_AI_TOKEN = 'YOUR_WIT_AI_SERVER_ACCESS_TOKEN'
Replace it with your actual Wit.ai server access token.
🖥️ Step 4: Run the Flask App
In terminal:
python app.py
This will start a local server at:
http://127.0.0.1:5000/
🌐 Step 5: Start Ngrok
In another terminal window:
ngrok http 5000
It will give you a public URL like:
https://8ef1-139-135-59-185.ngrok-free.app
☎️ Step 6: Configure Twilio
Go to Twilio Console > Phone Numbers

Under "A call comes in", select Webhook.

Paste the full ngrok link + /voice
Example:
https://8ef1-139-135-59-185.ngrok-free.app/voice
Save settings.
📞 Step 7: Test It
Call your Twilio number and say:

"Hi, my name is Ali. I live on Main Street. I want an appointment at 4 p.m."

The bot will:

Greet you

Listen

Save your name, address, and time to appointments.csv

📌 Notes
Keep the Flask and Ngrok windows open. If you close them, the bot won't work.

Make sure your Wit.ai app is trained to recognize:

name

datetime

location

📂 File Structure
├── app.py              # Main Flask app
├── appointments.csv    # Output file for saved data
├── README.md           # This guide
🧠 Future Ideas
Use Google Sheets instead of CSV

Add SMS confirmation

Add error handling

Deploy on cloud (like Heroku or Render)

🙋‍♂️ Questions?
Feel free to open an issue or contribute to improve this!

---

Let me know your GitHub repo name if you'd like me to update the `git clone` link above!


