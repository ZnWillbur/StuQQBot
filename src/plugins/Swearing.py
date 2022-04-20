from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot import on_regex, on_startswith
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment

swe1 = on_regex(r"woc|草|wc|艹")
swe2 = on_regex(r"操|靠|wok|wk")
swe3 = on_regex(r"离谱")

@swe1.handle()
async def handle_first_receive(bot: Bot, event: GroupMessageEvent):
    message = Message([
    MessageSegment(type='text', data={'text':'大草'})])
    await bot.send(event=event, message=message)


@swe2.handle()
async def handle_first_receive(bot: Bot, event: GroupMessageEvent):
    message = Message([
    MessageSegment(type='text', data={'text':'我们要做文明人哦'})])
    await bot.send(event=event, message=message)

@swe3.handle()
async def handle_first_receive(bot: Bot, event: GroupMessageEvent):
    message = Message([
    MessageSegment(type='text', data={'text':'离离原上谱'})])
    await bot.send(event=event, message=message)