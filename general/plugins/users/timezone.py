from nonebot import on_command, CommandSession
from .data_source import *

# on_command 装饰器将函数声明为一个命令处理器
# 这里 timezone 为命令的名字
@on_command('timezone', aliases=('time', 'tz'))
async def timezone(session: CommandSession):
    timezone = session.get('timezone', prompt='你现在是在哪个时区呢？')
    if not isinstance(timezone, int):
        await session.send('请原谅我并不明白你是什么意思。')
    user = session.get('user')
    timezone_report = await process_timezone(user, timezone)
    nickname = await utils.get_display_name(session)
    await session.send(nickname + timezone_report)

# timezone.args_parser 装饰器将函数声明为 timezone 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@timezone.args_parser
async def _(session: CommandSession):
    session = await utils.get_stated_session(session)
    stripped_arg = session.current_arg_text.strip()

    if stripped_arg and (stripped_arg.isdigit() or ((stripped_arg[0] in ['+', '-']) and stripped_arg[1:].isdigit())):
        session.state['timezone'] = int(stripped_arg)
        return
    else:
        session.pause('……我想我不太明白。你现在是在哪个时区呢？')