from ...plugins import utils
from ..utils import *
import random

async def get_r_report(r_count: int, r_max: int) -> str:
    r_results = []
    for i in range(r_count):
        r_results.append((random.randint(1, r_max)))
    r_sum = str(sum(r_results))
    r_results = [str(i) for i in r_results]
    r_report = str(r_count) + 'D' + str(r_max) + ': ' + '+'.join(r_results) + '=' + r_sum
    return r_report

async def get_text_rac_report(rac_rate: int, rac_text: str, msg: dict) -> str:
    rac_result = random.randint(1, 100)

    if rac_result <= 1:
        msg = msg['critical']
    elif rac_result <= rac_rate/5:
        msg = msg['extreme']
    elif rac_result <= rac_rate/2:
        msg = msg['hard']
    elif rac_result <= rac_rate:
        msg = msg['regular']
    elif rac_result >= 96:
        msg = msg['fumble']
    else:
        msg = msg['failure']
    
    msg = await utils.get_random_entry(msg)
    rac_report = '进行<' + rac_text + ">检定: D100=" + str(rac_result) + "/" + str(rac_rate) + '\n' + msg
    return rac_report