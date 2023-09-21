import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    def load_json(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program["occupation"])

        return programs_list
    
# programs = GetRequester()
# programs_occupation = programs.load_json()

# for occupation in set(programs_occupation):
#     print(occupation)
    