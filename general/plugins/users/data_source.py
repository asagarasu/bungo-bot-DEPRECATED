from ...plugins import utils
from ..utils import *

async def get_timezone_report(user: str) -> str:
    local = await utils.get_local_time(user)
    fmt = '%H:%M'
    local_fmt = local.strftime(fmt)
    timezone_report = f'那边现在是{local_fmt}对吗？'
    return timezone_report + "我已经记下了。"

async def process_timezone(user: str, tz: int) -> str:
    await utils.save_users_data(user, 'timezone', tz) 
    timezone_report = await get_timezone_report(user)
    return timezone_report

async def get_nickname_report(user: str) -> str:
    nickname = await utils.get_nickname(user)
    nickname_report = f'{nickname}，挺可爱的名字。我会记得的。'
    return nickname_report

async def process_nickname(user: str, nickname: str) -> str:
    await utils.save_users_data(user, 'nickname', nickname) 
    nickname_report = await get_nickname_report(user)
    return nickname_report
