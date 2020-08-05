from nonebot.default_config import *
from datetime import timedelta

SESSION_EXPIRE_TIMEOUT = timedelta(minutes=1)
SHORT_MESSAGE_MAX_LENGTH = 100
DEFAULT_VALIDATION_FAILURE_EXPRESSION = ''
COMMAND_START = {"#", "."}
COMMAND_SEP = {'-'}
HOST = '127.0.0.1'
PORT = 8000