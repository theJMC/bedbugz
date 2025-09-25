from fastapi import FastAPI
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
client = OpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{bug}")
async def root(bug):
    response = client.responses.create(
        model="o4-mini",
        input="Please generate 6 of the below response. You are pretending to be an insect bug on tinder. You are a [bug]. Please can you generate a message \
        from you, the bug, to another bug. Can you try to keep the responses concise please. Please respond exactly in the format \
        {'bugMsg': 'MESSAGE','responses': \
        {'good': 'GOOD_RESPONSE','medium': 'MEDIUM_RESPONSE','bad': 'BAD_RESPONSE'}}".replace("[bug]", bug)
    )
    results = []
    for res in response.output_text.split("\n"):
        results.append(res)
    return results

