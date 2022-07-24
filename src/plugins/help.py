from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, PrivateMessageEvent, MessageSegment

text = """使用指南：
1.nonebot_plugin_petpet
请发送：“头像表情包”以获取使用方法

2.nonebot_plugin_emojimix
请发送:“（emoji1）+（emoji2）”以获得混合emoji

3.nonebot_plugin_pixivrank_search
请发送:“P站排行榜帮助”、“搜图帮助”以获取使用方法

4.AdoingB(内置)
请发送：“/字符串1 (字符串2,可选) @xxx”
回复：“@你自己 字符串1 @xxx 字符串2 ！”
"""

GroupIncrease = on_command("help")

@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupMessageEvent):
    message = Message([
    MessageSegment(type='text', data={'text':text})])
    await bot.send(event=event, message=message)
