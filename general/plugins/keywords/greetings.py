from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import *
from ...plugins import utils

# good morning
@on_command('morning', only_to_me=False)
async def morning(session: CommandSession):
    data = await utils.load_keywords_data('greetings')
    msg_morning = data['morning']
    user = session.get('user')
    msg_is_morning = await get_is_morning(msg_morning, user)
    nickname = await utils.get_display_name(session)
    msg = nickname + msg_is_morning
    await session.send(msg)

@on_natural_language(keywords={'早安', '早上好'}, only_to_me=False)
async def _(session: NLPSession):
    if session.event['to_me'] or utils.get_random_boolean(50):
        return IntentCommand(100.0, 'morning')

# good night
@on_command('night', only_to_me=False)
async def night(session: CommandSession):
    data = await utils.load_keywords_data('greetings')
    msg_night = data['night']
    user = session.get('user')
    msg_is_night = await get_is_night(msg_night, user)
    nickname = await utils.get_display_name(session)
    msg = nickname + msg_is_night
    await session.send(msg)

@on_natural_language(keywords={'晚安', '睡了'}, only_to_me=False)
async def _(session: NLPSession):
    if session.event['to_me'] or utils.get_random_boolean(50):
        return IntentCommand(100.0, 'night')

@morning.args_parser
@night.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)