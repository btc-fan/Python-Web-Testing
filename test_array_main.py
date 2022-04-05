import json

import pytest
from conftest import *
from test_main import test_main
from utils.variables import DATA_MODEL_FOLDER

if __name__ == '__main__':

    json_file = open(DATA_MODEL_FOLDER + "person_data_array.json")
    person_data_array = json.load(json_file)
    # for person_data in person_data_array:
    #     pytest.main(["test_main.py", f"--person_data={json.dumps(person_data)}"])
    # run_person(browser, person_data)
    # pytest.main(["test_main.py"])


    # json_file = open(DATA_MODEL_FOLDER + "person_data_array.json")
    # person_data_array = json.load(json_file)
    # for person in person_data_array:
    #     test_main(browser, user_json_path, person)

    # pytest_args =[
    #     "test_main.py",
    #     "--user_json_path=/Users/techquarter/Desktop/gl_work_projects/heimdall-empty/heimdall-automation/utils/data_models/person_data_model.json"
    # ]

    # pytest.main(pytest_args)
    pytest.main(['-q', '-s', '--user_json_path', "args_string", 'test_main.py'])
