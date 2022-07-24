from nonebot import on_command
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import Bot, PrivateMessageEvent, MessageSegment


PrivateIncrease =  on_command("打卡")

@PrivateIncrease.handle()
async def phelp(bot: Bot, event:PrivateMessageEvent):
    for i in range(1, 67):
        message = Message([
            MessageSegment(type='text', data={'text':f"打卡{i}"})])
        await bot.send(event=event, message=message)