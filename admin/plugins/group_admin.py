from nonebot import on_notice, NoticeSession
from nonebot.log import logger
from .utils import *

@on_notice
async def _(session: NoticeSession):
    logger.info('new notice: %s', session.event)

@on_notice('group_decrease')
async def _(session: NoticeSession):
    msg = await load_admin_data("group_decrease")
    await session.send(msg)
    return

@on_notice('group_increase.invite')
async def _(session: NoticeSession):
    if session.event['self_id'] == session.event['user_id']:
        msg = await load_admin_data("add_group")
    else:
        msg = await load_admin_data("group_increase")
    await session.send(msg)
    return