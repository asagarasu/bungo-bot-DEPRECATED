# bungo-bot[DEPRECATED]

## Overview

Bungo-bot was a QQ-based bot project developed based on the [CQHTTP](https://github.com/richardchien/coolq-http-api) plugin which enabled receiving events from [CoolQ](https://github.com/CoolQ/docker-wine-coolq) through HTTP or reverse proxy WebSocket connection. It included features such as dice roll, keyword reply and random deck draw with a decently automated admin manipulation. 

This project was halted on August 4th, 2020 due to [a single-sided incident](https://www.zhihu.com/question/411466505)([PDF](https://github.com/yilin-lu/bungo-bot-DEPRECATED/blob/master/docs/%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%E8%BF%91%E6%9C%9F%E5%A4%A7%E9%87%8F%E7%9A%84%E7%AC%AC%E4%B8%89%E6%96%B9QQ%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%81%9C%E6%AD%A2%E8%BF%90%E8%90%A5%EF%BC%9F%20-%20%E7%9F%A5%E4%B9%8E.pdf)) between Tencent and a number of third-party developers. As CoolQ and other plugins terminating their service, it is, unfortunately, senseless to continue developing any QQ-based projects.

## Dependencies

The main dependencies were Python(3.7.7), [Nonebot(1.6.0)](https://github.com/nonebot/nonebot) and PyYAML(5.3.1). [A YAML file](https://github.com/yilin-lu/bungo-bot-DEPRECATED/blob/master/environment.yaml) of the full conda environment "bot" is generated.

A notable change happened in Nonebot's `parse_command` function under its `nonebot>command>__init__.py` package. The changed file is [here](https://github.com/yilin-lu/bungo-bot-DEPRECATED/blob/master/docs/__init__.py). 

## Installation and Running

Clone the repository, install and activate the conda environment, manually re-install the changed version of Nonebot, run and login CoolQ, and run the bot.py file at the root directory of this repository.

By August 4th, 2020, the procedure is no longer available.

## Code Structure

```
bungo-bot
- bot.py
- config.py
- admin
	- data
	- plugins
		- some-plugin.py
		- utils.py
- general
	- data
		- deck
	- plugins
		- some-plugin.py
		- utils.py
```

Data, or pre-written responses, were stored under respective data folders in json format. "Deck" data were in YAML format due to the legacy from [SinaNya](https://sinanya.com/) with a restriction of only supporting internal variables in the given format.  Each package of plugins had its own set of utils.

## Plugins

### Commands

All commands could be triggered with a prefix of a dot sign `.` or a hashtag `#`. The dot sign prefix could be turned off by group or private chat through an admin command. The backslash separates alias for the same command.

#### admin

Command | Effect | Permission | Only to me
------------ | -------------  | ------------- | -------------
mode inclusive | Switch the command prefix to both dot and hashtag at the current window | super, owner, admin | Yes 
mode exclusive | Switch the command prefix to hashtag only at the current window | super, owner, admin | Yes 

#### general

Command | Effect | Only to me
------------ | -------------  | -------------
deck | Trigger a random deck draw given the following two parameters, such as `.deck 雷诺曼 两张纸牌`. When no parameters or invalid ones are given, respond with respective instructions. | No 
r/roll | Trigger a random dice roll given the following one parameter, such as `.roll 2d3` will roll two dice of 3 faces. When no parameter is given, roll a single dice of 100 faces. | No 
rac/ra/rc | Trigger a random dice roll given the following two parameter, such as `.ra message 80` will roll one dice of 80 faces along the given message. | No 
nickname/name/nn | Change and store the parameter as the nickname of the user. | Yes 
timezone/time/tz | Change and store the parameter(must be an integer) as the timezone of the user. | Yes 

### Natural Language Processing

All NLP plugins could be triggered by keywords detected from sentences. Complicated responses were yet to be built.

Check `general>plugins>keywords` to see the available rule-based plugins.

### Other features

- automatic approval of friend requests and group invitations
- automatic message for new friends, new groups and group member changes
- varied responses to greetings depends on users' logged timezones

## Known Problems

- does not avoid parsing other bots' message
- too rigid a rule for calling the bot
- does not ignore users' responds to other users' "good night"

## Future Visions

As the name suggested, this was a project inspired from Bungo To Alchemist, a 2020 anime show. The origin plan was to develop a Bungo persona by taking advantages of I-novel and letter datasets after the general dice bot features were completed. 

However, given the current circumstance, it does not make sense to continue the development. In the foreseeable future, the bungo-bot project will be migrated to Discord with a rule-based persona. Whether branching out to WeChat or other platforms remains unknown at the moment.
