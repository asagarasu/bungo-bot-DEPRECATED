from nonebot import on_request, RequestSession
from nonebot.log import logger
from .utils import *

@on_request
async def _(session: RequestSession):
    logger.info('new request: %s', session.event)

@on_request('friend')
async def _(session: RequestSession):
    await session.approve()
    msg = await load_admin_data("add_friend")
    await session.send(msg)
    return

@on_request('group.invite')
async def _(session: RequestSession):
    await session.approve()
    msg = await load_admin_data("add_group")
    await session.send(msg)
    return
