import requests as r

API_BASE_URL = "https://api.inaturalist.org/v1"

# API_PROJECT_ID = "bu-nature-hackathon-2025"
API_PROJECT_ID = "bournemouth-university-campus-biodiversity-network"

req = r.get(API_BASE_URL + f"/observations?project_id={API_PROJECT_ID}&order=desc&order_by=created_at")
res = req.json()

for i in res["results"]:
    try:
        print(f"{i['uuid']} - species: {i['species_guess']} - {i['taxon']['wikipedia_url']}")
    except TypeError:
        print(f"{i['uuid']} - species: {i['species_guess']}")

print(len(res["results"]))