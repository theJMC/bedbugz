import base64
import json
import math
import os

API_BASE_URL = "https://api.inaturalist.org/v1"
API_PROJECT_ID = "bournemouth-university-nature-hackathon-2025"
API_CALL_LIMIT = 10

from fastapi import FastAPI
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
import requests as r

client = OpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
{'bugMsg': 'MESSAGE','responses': \
        {'good': 'GOOD_RESPONSE','medium': 'MEDIUM_RESPONSE','bad': 'BAD_RESPONSE'}}"
"""

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat/{bug}")
async def get_bug(bug):
    response = client.responses.create(
        model="o4-mini",
        input="Please generate 6 of the below response. You are pretending to be an insect bug on tinder. You are a [bug]. Please can you generate a message \
        from you, the bug, to another bug. Can you try to keep the responses concise please. Please respond exactly in the format \
        Please respond in JSON format, with a string field 'bugMsg', then a dict called 'responses' which contains 'good', 'medium', 'bad'.".replace("[bug]", bug)
    )
    result = json.loads(" ".join(response.output_text.split()))
    return result

@app.get("/profile/{page}")
async def profile(page: int):
    PER_PAGE = 5
    all_profiles = []
    with open(os.environ["JSON_LOC"]) as f:
        all_profiles = json.load(f)

    length = len(all_profiles)
    num_of_pages = math.ceil(length / PER_PAGE)
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    return {"num_of_pages": num_of_pages, "current_page": page, "profiles": all_profiles[start_index:end_index]}
