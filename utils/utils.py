import json
import os

from utils.logger import LOGGER
from utils.paths import DATA_MODEL_FOLDER, GENERATED_JSON_FOLDER, PERSON_DATA_ARRAY_JSON

JSON_USER_DATA = open(DATA_MODEL_FOLDER + "person_data_array.json")
JSON_RESPONSE_PATH = GENERATED_JSON_FOLDER + "response.json"

def inject_data():
    LOGGER.info("Looking for PERSON_DATA_ARRAY Env Variable:")
    with open(PERSON_DATA_ARRAY_JSON, 'r+') as f:
        person_data_array = json.load(f)
    return person_data_array

def get_current_object_index_by_uuid(test_data, uuid: str):
    list_index = test_data.index(next(filter(lambda n: n.get('UUID') == uuid, test_data)))
    return list_index

