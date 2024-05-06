# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

from dotenv import load_dotenv,find_dotenv
import os

import google.generativeai as genai

load_dotenv(find_dotenv("/home/hellopyt/mysite/api.env"))
api_key = os.getenv("API_KEY")

app = Flask(__name__)
@app.route('/')
def hello_world():
    history = str(request.args.get('input'))
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    generation_config = genai.GenerationConfig(temperature=0)

    prompt = "summarize the provided chat history between a user and the chatbot: "+str(history)+" as a report. here the chatbot's reponse is provided with key" \
    "'chatbot' and the user's reponse is given in key 'user'. the coversation between both is provided within '[]' corresponding to each of the response from 'user' and 'chatbot'. "\
    "With the chatbot, user provides and reports the information about the accident to the chatbot. The summarization should be accurate as per the data "\
    "provided as it is shared to the higher authorities. generate the report in first person. add 'description' which tells the decription about the accident,'damage','injuries',"\
    "'actions taken' based on the given data to the summarized report."

    response = model.generate_content(prompt, generation_config=generation_config)
    return "".join(response.text.split("**")).lstrip("## ")

