import requests as r
import json

API_BASE_URL = "https://api.inaturalist.org/v1"
API_PROJECT_ID = "bournemouth-university-nature-hackathon-2025"
API_CALL_LIMIT = 10

API_TAXAS = "Actinopterygii%2CAnimalia%2CAmphibia%2CArachnida%2CAves%2CChromista%2CFungi%2CInsecta%2CMammalia%2CMollusca%2CReptilia%2CProtozoa"

from openai import OpenAI

client = OpenAI()


class Profile:
    def __init__(self, name: str, species: str, images: list[str], description: str, prompts: list[dict[str, str]]):
        self.name = name
        self.species = species
        self.images = images
        self.description = description
        self.prompts = prompts

    def generate_prompts(self):
        self.prompts = []

    def to_json(self):
        return {
            "name": self.name,
            "species": self.species,
            "images": self.images,
            "description": self.description,
            "prompts": self.prompts
        },


def add_new_profile(page: int):
    req = r.get(
        API_BASE_URL + f"/observations?project_id={API_PROJECT_ID}&order=desc&order_by=created_at&iconic_taxa={API_TAXAS}&per_page=1&page={page}")
    # req = r.get(
    # API_BASE_URL + f"/observations?project_id={API_PROJECT_ID}&order=desc&order_by=created_at&per_page=1")
    if req.json()["total_results"] < page:
        raise Exception(f"Page {page} does not exist")

    try:
        bug = req.json()["results"][0]
    except IndexError:
        print(req.json())
    result = []
    try:
        name = bug["taxon"]["preferred_common_name"]
    except KeyError:
        name = bug["taxon"]["name"]

    photos = []
    try:
        photo_req = r.get(API_BASE_URL + "/taxa/" + str(bug["taxon"]["id"]))
        photo_res = photo_req.json()["results"][0]
        # print(photo_res["default_photo"]["medium_url"])
        photos.append(photo_res["default_photo"]["medium_url"])
        # for photo in photo_res["default_photo"]:
        #     print(photo)
        #     photos.append(photo["default_photo"]["medium_url"])
    except KeyError:
        print("USED KEY ERROR")
        for photo in bug["photos"]:
            photos.append(photo["url"])
            print(photo["url"])


    # description = bug["taxon"]["description"]
    description = f"Fun Fact! It's a {name}"

    # generate stuff
    spec_req = r.get(API_BASE_URL + "/taxa/" + str(bug["taxon"]["parent_id"]))
    spec_name = spec_req.json()["results"][0]["name"]

    response = client.responses.create(
        model="o4-mini",
        input="Please generate 3 dicts in the below json array. Generate a question and answer about a [bug].  \
            Please respond exactly in the format \
            Please respond in JSON format, as an array of dicts. the dict should contain two string fields, \
            one called question, another called answer.".replace("[bug]", name)
    )
    prompts = json.loads(" ".join(response.output_text.split()))

    return Profile(name, spec_name, photos, description, prompts)


def write_to_file(results):
    with open("new_profiles.json", "w+") as json_file:
        json.dump(results, json_file)


if __name__ == "__main__":
    results = []
    try:
        for i in range(23, 50):
            print(i)
            new = add_new_profile(i + 1)
            print(new.to_json()[0])
            results.append(new.to_json()[0])
    except KeyboardInterrupt as e:
        pass
    finally:
        write_to_file(results)
