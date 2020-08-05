from ...plugins import utils
from ..utils import *
import re
import random

def get_replaced(key, deck):
    values = deck[key[2:-1]]
    msg = values[random.randint(0,len(values)-1)]
    return msg

async def get_text_deck_report(deck_name: str, deck_command: str) -> str:
    deck = await utils.load_deck(deck_name)
    if deck_command in deck:
        master = await utils.get_random_entry(deck[deck_command])
        master = re.sub(r'\{\$\_.*?\}', lambda m: get_replaced(m.group(), deck), master)
        return master
    return ""
        