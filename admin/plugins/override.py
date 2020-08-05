from nonebot.command import *
from .utils import *

def parse_command(self, bot: NoneBot,
    event: CQEvent) -> Tuple[Optional[Command], Optional[str]]:

    cmd_string = str(event.message).lstrip()
    logger.debug(f'Hijacked Parsing command: {repr(cmd_string)}')
    matched_start = None

    id_str = get_id_str(event)
    CONFIG = load_config_data(id_str)

    if "COMMAND_START" in CONFIG:
        COMMAND_START = CONFIG["COMMAND_START"]
    else:
        COMMAND_START = bot.config.COMMAND_START

    for start in COMMAND_START:
        # loop through COMMAND_START to find the longest matched start
        curr_matched_start = None
        if isinstance(start, type(re.compile(''))):
            m = start.search(cmd_string)
            if m and m.start(0) == 0:
                curr_matched_start = m.group(0)
        elif isinstance(start, str):
            if cmd_string.startswith(start):
                curr_matched_start = start

        if curr_matched_start is not None and \
                (matched_start is None or
                len(curr_matched_start) > len(matched_start)):
            # a longer start, use it
            matched_start = curr_matched_start

    if matched_start is None:
        # it's not a command
        logger.debug('It\'s not a command')
        return None, None

    logger.debug(f'Matched command start: '
                f'{matched_start}{"(empty)" if not matched_start else ""}')
    full_command = cmd_string[len(matched_start):].lstrip()

    if not full_command:
        # command is empty
        return None, None

    cmd_name_text, *cmd_remained = full_command.split(maxsplit=1)

    cmd_name = None
    for sep in bot.config.COMMAND_SEP:
        # loop through COMMAND_SEP to find the most optimized split
        curr_cmd_name = None
        if isinstance(sep, type(re.compile(''))):
            curr_cmd_name = tuple(sep.split(cmd_name_text))
        elif isinstance(sep, str):
            curr_cmd_name = tuple(cmd_name_text.split(sep))

        if curr_cmd_name is not None and \
                (not cmd_name or len(curr_cmd_name) > len(cmd_name)):
            # a more optimized split, use it
            cmd_name = curr_cmd_name

    if not cmd_name:
        cmd_name = (cmd_name_text,)
    logger.debug(f'Split command name: {cmd_name}')

    cmd = self._find_command(cmd_name)  # type: ignore
    if not cmd:
        logger.debug(f'Command {cmd_name} not found. Try to match aliases')
        cmd = {
            name: cmd
            for name, cmd in self.aliases.items()
            if self.switches.get(cmd, True)
        }.get(cmd_name_text)

    if not cmd:
        logger.debug(f'Alias {cmd_name} not found. Try to match patterns')
        patterns = {
            pattern: cmd
            for pattern, cmd in self.patterns.items()
            if self.switches.get(cmd, True)
        }
        for pattern in patterns:
            if pattern.search(full_command):
                cmd = patterns[pattern]
                logger.debug(
                    f'Pattern {pattern} of command {cmd.name} matched, function: {cmd.func}'
                )
                # if command matched by regex, it will use the full_command as the current_arg of the session
                return cmd, full_command

    if not cmd:
        return None, None

    logger.debug(f'Command {cmd.name} found, function: {cmd.func}')
    return cmd, ''.join(cmd_remained)


CommandManager.parse_command = parse_command
