from nonebot import on_command, CommandSession
from .data_source import *
from ...plugins import utils

# on_command 装饰器将函数声明为一个命令处理器
# 这里 deck 为命令的名字，同时允许使用别名
@on_command('deck', only_to_me=False)
async def deck(session: CommandSession):
    data = await utils.load_deck_data()
    is_valid = session.get('is_valid')
    is_command = session.get('is_command')
    if not is_valid:
        msg = await utils.get_random_entry(data['error'])
        await session.send(msg)
        return
    else:
        deck_name = session.get('deck_name')
        if is_command:
            deck_command = session.get('deck_command')
            deck_report = await get_text_deck_report(deck_name, deck_command)
        else:
            deck_report = await get_text_deck_report(deck_name, "default")
        if not deck_report:
            msg = await utils.get_random_entry(data['error'])
            await session.send(msg)
            return
        nickname = await utils.get_display_name(session)
        await session.send('[' + nickname + ']' + deck_report)

# deck.args_parser 装饰器将函数声明为 deck 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@deck.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)

    stripped_arg = session.current_arg_text.strip()
    split_arg = stripped_arg.split()

    session.state['is_valid'] = True
    session.state['is_command'] = True
    
    if len(split_arg) == 2:
        session.state['deck_name'] = str(split_arg[0])
        session.state['deck_command'] = str(split_arg[1])
    elif len(split_arg) == 1:
        session.state['deck_name'] = str(split_arg[0])
        session.state['is_command'] = False
    else: 
        session.state['is_valid'] = False