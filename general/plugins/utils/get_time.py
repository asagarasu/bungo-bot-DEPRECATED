from datetime import datetime, timedelta, timezone
from .load_data import *

async def get_local_time(user: str) -> datetime:
    tz = await load_user_data(user, "timezone")
    utc = datetime.now(timezone.utc)
    if tz:
        shift = timedelta(hours=tz)
    else:
        shift = timedelta(hours=8)
    local = utc + shift
    return local

async def get_local_hour(user: str) -> int:
    local_time = await get_local_time(user)
    return local_time.hour