from nonebot import on_command, CommandSession
from .data_source import *

@on_command('nickname', aliases=('name', 'nn'))
async def nickname(session: CommandSession):
    nickname = session.get('nickname')
    user = session.get('user')
    nickname_report = await process_nickname(user, nickname)
    await session.send(nickname_report)

@nickname.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    session = await utils.get_stated_session(session)

    if stripped_arg:
        session.state['nickname'] = str(stripped_arg)