from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
import requests
import json
import csv
import os

app = Flask(__name__)

WIT_AI_TOKEN = 'YOUR_WIT_AI_SERVER_ACCESS_TOKEN'

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    gather = Gather(input="speech", timeout=5, speechTimeout="auto", action="/gather", method="POST")
    gather.say("Hello! This is the clinic. Please tell me your name, address, and preferred time for appointment.")
    response.append(gather)
    response.redirect('/voice')
    return Response(str(response), mimetype='application/xml')

@app.route("/gather", methods=['POST'])
def gather():
    speech_text = request.form.get('SpeechResult')
    print("User said:", speech_text)

    # Send to Wit.ai for entity extraction
    headers = {"Authorization": f"Bearer {WIT_AI_TOKEN}"}
    res = requests.get(f"https://api.wit.ai/message?v=20200513&q={speech_text}", headers=headers)
    wit_data = res.json()
    
    # Simple extraction (you can improve based on your entities)
    name = wit_data['entities'].get('name:name', [{}])[0].get('value', '')
    time = wit_data['entities'].get('wit$datetime:datetime', [{}])[0].get('value', '')
    address = wit_data['entities'].get('location:location', [{}])[0].get('value', '')
    
    # Save to CSV
    with open('appointments.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, address, time, speech_text])

    response = VoiceResponse()
    response.say("Thank you. Your appointment has been noted. Goodbye!")
    return Response(str(response), mimetype='application/xml')

if __name__ == "__main__":
    app.run(debug=True)
