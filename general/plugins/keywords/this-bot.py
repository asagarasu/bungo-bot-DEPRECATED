from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .data_source import *
from ...plugins import utils

@on_command('this_bot', aliases=('bot'), only_to_me=False)
async def this_bot(session: CommandSession):
    data = await utils.load_keywords_data('this_bot')
    msg = data['call']
    msg = await utils.get_random_entry(msg)
    request = session.get('request', prompt=msg)
    this_bot_report = await get_this_bot(data, request)
    nickname = await utils.get_display_name(session)
    await session.send(nickname + this_bot_report)

@this_bot.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)
    stripped_arg = session.event['raw_message'].strip()
    for i in ['this_bot', 'bot']:
        stripped_arg = stripped_arg.replace(i, '')
    if stripped_arg:
        session.state['request'] = stripped_arg

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'this_bot', 'bot'}, only_to_me=False)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(100.0, 'this_bot')
