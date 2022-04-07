import os
import json
import pytest

def getPayload():
    # json_file = open(DATA_MODEL_FOLDER + "person_data_array.json")
    # person_data_array = json.load(json_file)
    varName='MY_PAYLOAD'
    person_data_array = json.loads(os.environ.get(varName))
    return person_data_array

def processDataRecord(person_data):
    print(person_data)
    os.environ['REQUEST'] = json.dumps(person_data)
    pytest.main(['-q', '-s', '--user_json_path', "args_string", 'test_main.py'])

def processPayload(payload):
    for person_data in payload:
        processDataRecord(person_data)
        
def main():
    processPayload(getPayload())

if __name__ == '__main__':
    main()