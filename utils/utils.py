import json

from utils.variables import DATA_MODEL_FOLDER, GENERATED_JSON_FOLDER

JSON_USER_DATA = open(DATA_MODEL_FOLDER + "person_data_array.json")
JSON_RESPONSE_PATH = GENERATED_JSON_FOLDER + "response.json"

def inject_data():
    person_data_array = json.load(JSON_USER_DATA)
    return person_data_array

# def write_captcha_json(new_data, json_response=JSON_RESPONSE_PATH):
#     with open(json_response, 'a+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["captcha"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 4)

def get_current_object_index_by_uuid(test_data, uuid: str):
    list_index = test_data.index(next(filter(lambda n: n.get('UUID') == uuid, test_data)))
    return list_index

