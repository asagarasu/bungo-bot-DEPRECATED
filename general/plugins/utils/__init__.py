from nonebot import CommandSession
from .load_data import *
from .get_time import *
import random

__all__ = ["load_data", "get_time"]

async def get_random_entry(msg: list) -> str:
    msg = msg[random.randint(0,len(msg)-1)]
    return msg

async def get_random_boolean(success: int) -> bool:
    roll = random.randint(1, 100)
    return roll < success
    
async def get_nickname(user: str) -> object:
    nickname = await load_user_data(user, "nickname")
    return nickname

async def get_display_name(session: CommandSession) -> str:
    user = session.get("user")
    nickname = await get_nickname(user)
    if nickname:
        return str(nickname)
    else:
        return str(session.get("nickname"))

async def get_stated_session(session: CommandSession) -> CommandSession:
    user = session.event['user_id']
    session.state['user'] = str(user)
    nickname = session.event['sender']['nickname']
    session.state['nickname'] = nickname
    return session