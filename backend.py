import streamlit as st
import openai
import os
from dotenv import load_dotenv

class ChatGPT:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("openai_APIKEY")

    def generate_response(self, prompt, model="gpt-3.5-turbo-0125"):
        openai.api_key = self.api_key
        response = openai.completions.create(
            model=model,
            prompt=prompt
        )
        return response.choices[0].message.content


