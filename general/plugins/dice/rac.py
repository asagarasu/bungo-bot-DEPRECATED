from nonebot import on_command, CommandSession
from .data_source import *
from ...plugins import utils

# on_command 装饰器将函数声明为一个命令处理器
# 这里 rac 为命令的名字，同时允许使用别名
@on_command('rac', aliases=('ra', 'rc'), only_to_me=False)
async def rac(session: CommandSession):
    data = await utils.load_dice_data()
    is_valid = session.get('is_valid')
    if not is_valid:
        msg = await utils.get_random_entry(data['error'])
        await session.send(msg)
    else:
        rac_rate = session.get('rac_rate')
        rac_text = session.get('rac_text')
        rac_report = await get_text_rac_report(rac_rate, rac_text, data['msg'])
        nickname = await utils.get_display_name(session)
        await session.send('[' + nickname + ']' + rac_report)

# rac.args_parser 装饰器将函数声明为 rac 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@rac.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)

    stripped_arg = session.current_arg_text.strip()
    split_arg = stripped_arg.split()

    session.state['rac_count'] = 1
    session.state['rac_max'] = 100
    session.state['is_valid'] = True
    
    if len(split_arg) == 2:
        if split_arg[1].isdigit():
            session.state['rac_rate'] = int(split_arg[1])
            session.state['rac_text'] = split_arg[0]
            session.state['is_text'] = True
        else:
            session.state['is_valid'] = False
    
    else: 
        session.state['is_valid'] = False