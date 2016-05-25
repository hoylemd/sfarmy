import json


def write_to_json_file(obj, file_name):
    seps = (',', ': ')
    serialized = json.dumps(obj, sort_keys=True, indent=2, separators=seps)

    with open(file_name, 'w') as f:
        f.write(serialized)


def read_from_json_file(file_name):
    with open(file_name) as f:
        payload = json.loads(f.read())

    return payload
