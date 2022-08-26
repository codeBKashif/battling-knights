import json


from os import path

output_file = path.join(path.dirname(__file__), "data/final_state.json")


def write_output(output):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output, file)
