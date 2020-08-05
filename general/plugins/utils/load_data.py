import json
import os
import yaml

data_path = './general/data'

async def load_user_data(user: str, key: str) -> object:
    with open(os.path.join(data_path, 'users.json')) as f:
        data = json.load(f)
    if user in data:
        if key in data[user]:
            return data[user][key]
    return None

async def save_users_data(user: str, key: str, value: int) -> None:
    with open(os.path.join(data_path, 'users.json')) as f:
        data = json.load(f)
    if user in data:
        data[user][key] = value
    else:
        data[user] = {key: value}
    with open(os.path.join(data_path, 'users.json'), 'w') as f:
        json.dump(data, f)

async def load_dice_data() -> dict:
    with open(os.path.join(data_path, 'dice.json')) as f:
        data = json.load(f)
    return data

async def load_keywords_data(key: str) -> dict:
    with open(os.path.join(data_path, 'keywords.json')) as f:
        data = json.load(f)
    return data[key]

async def load_deck_data() -> dict:
    with open(os.path.join(data_path, 'deck.json')) as f:
        data = json.load(f)
    return data

async def load_deck(key: str) -> dict:
    deck_name = key + ".yaml"
    try:
        with open(os.path.join(data_path, 'deck', deck_name)) as f:        
            deck_data = yaml.load(f, Loader=yaml.FullLoader)
            return deck_data
    except:
        return {}