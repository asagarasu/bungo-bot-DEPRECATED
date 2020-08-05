import json
import os

data_path = './admin/data'

async def load_admin_data(key: str) -> object:
    with open(os.path.join(data_path, 'admin.json')) as f:
        data = json.load(f)
    return data[key]

def load_config_data(key: str) -> object:
    with open(os.path.join(data_path, 'config.json')) as f:
        data = json.load(f)
    if key in data:
        return data[key]
    else:
        return {}

async def save_config_data(id_str: str, key: str, value: object) -> None:
    with open(os.path.join(data_path, 'config.json')) as f:
        data = json.load(f)
    if id_str in data:
        data[id_str][key] = value
    else:
        data[id_str] = {key: value}
    with open(os.path.join(data_path, 'config.json'), 'w') as f:
        json.dump(data, f)

def get_id_str(event):
    if "group_id" in event:
        return str(event["group_id"])
    else:
        return str(event["user_id"])
