from fastapi import FastAPI
from openai import OpenAI
client = OpenAI()
app = FastAPI()

@app.get("/{bug}")
async def root(bug):
    response = client.responses.create(
        model="gpt-5-nano",
        input="You are pretending to be an insect bug on tinder. You are a [bug]. Please can you generate a message \
        from you, the bug, to another bug. Can you try to keep the responses concise please. Please respond exactly in the format \
        {'bugMsg': 'MESSAGE','responses': \
        {'good': 'GOOD_RESPONSE','medium': 'MEDIUM_RESPONSE','bad': 'BAD_RESPONSE'}}".replace("[bug]", bug)
    )
    return response.output_text

