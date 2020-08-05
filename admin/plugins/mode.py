from nonebot import on_command, CommandSession, CommandGroup
from nonebot import permission as perm
from nonebot.plugin import PluginManager
from nonebot import message_preprocessor
from nonebot.log import logger
from .utils import *

mode = CommandGroup('mode')

@mode.command(
    'exclusive', 
    permission=perm.SUPERUSER|perm.GROUP_OWNER|perm.GROUP_ADMIN, 
    only_to_me=True, 
    privileged=True
    )
async def _(session: CommandSession):
    id_str = get_id_str(session.event)
    await save_config_data(id_str, "COMMAND_START", ["#"])
    msg = await load_admin_data("exclusive")
    await session.send(msg)

@mode.command(
    'inclusive', 
    permission=perm.SUPERUSER|perm.GROUP_OWNER|perm.GROUP_ADMIN, 
    only_to_me=True, 
    privileged=True
    )
async def _(session: CommandSession):
    id_str = get_id_str(session.event)
    await save_config_data(id_str, "COMMAND_START", ["#", "."])
    msg = await load_admin_data("inclusive")
    await session.send(msg)

'''
@mode.command(
    'off', 
    permission=perm.SUPERUSER|perm.GROUP_OWNER|perm.GROUP_ADMIN, 
    only_to_me=True, 
    privileged=True
    )
async def _(session: CommandSession):
    PluginManager.switch_plugin("./general/plugins", state=False)
    await session.send("现在general插件已关闭")

@mode.command(
    'on', 
    permission=perm.SUPERUSER|perm.GROUP_OWNER|perm.GROUP_ADMIN, 
    only_to_me=True, 
    privileged=True
    )
async def _(session: CommandSession):
    PluginManager.switch_plugin("./general/plugins", state=True)
    await session.send("现在general插件已开启")
'''