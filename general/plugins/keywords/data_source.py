from ...plugins import utils

async def get_is_morning(data: dict, user: str) -> int:
    local_hour = await utils.get_local_hour(user)
    if local_hour < 6:
        msg = await utils.get_random_entry(data['early'])
        return msg + "你那里现在是" + str(local_hour) + "点吧？"
    elif local_hour > 11:
        msg = await utils.get_random_entry(data['late'])
        return msg + "你那里现在可是" + str(local_hour) + "点了。"
    else:
        msg = await utils.get_random_entry(data['ok'])
        return msg

async def get_is_night(data: dict, user: str) -> int:
    local_hour = await utils.get_local_hour(user)
    if local_hour >= 1 and local_hour < 6:
        msg = await utils.get_random_entry(data['late'])
        return msg + "已经" + str(local_hour) + "点都过了。"
    elif local_hour > 20 or local_hour < 1:
        msg = await utils.get_random_entry(data['ok'])
        return msg
    else:
        msg = await utils.get_random_entry(data['early'])
        return msg

async def get_kmmso(data: dict, stripped_arg: str) -> str:
    for key in data['keys'].keys():
        if key in stripped_arg:
            key = data['keys'][key]
            msg = data['request'][key]
            msg = await utils.get_random_entry(msg)
            return msg
    msg = data['blank']
    msg = await utils.get_random_entry(msg)
    return msg
