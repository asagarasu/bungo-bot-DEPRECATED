from nonebot import on_command, CommandSession
from .data_source import *
from ...plugins import utils

# on_command 装饰器将函数声明为一个命令处理器
# 这里 r 为命令的名字，同时允许使用别名
@on_command('r', aliases=('roll'), only_to_me=False)
async def r(session: CommandSession):
    data = await utils.load_dice_data()
    is_valid = session.get('is_valid')

    if not is_valid:
        msg = await utils.get_random_entry(data['error'])
        await session.send(msg)

    else:
        r_count = session.get('r_count')
        r_max = session.get('r_max')
        r_report = await get_r_report(r_count, r_max)
        nickname = await utils.get_display_name(session)
        await session.send('[' + nickname + ']' + r_report)

# r.args_parser 装饰器将函数声明为 r 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@r.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)
        
    stripped_arg = session.current_arg_text.strip()
    split_arg = stripped_arg.split()
    session.state['r_count'] = 1
    session.state['r_max'] = 100
    session.state['is_valid'] = True

    if len(split_arg) > 1:
        session.state['is_valid'] = False
  
    elif len(split_arg) == 1:
        r_stats = split_arg[0].lower()
        r_stats = r_stats.split('d')
        if len(r_stats) == 2 and r_stats[0].isdigit() and r_stats[1].isdigit():
            session.state['r_count'] = int(r_stats[0])
            session.state['r_max'] = int(r_stats[1])
        else:
            session.state['is_valid'] = False