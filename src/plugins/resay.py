from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent
from nonebot import on_regex
from nonebot.matcher import Matcher

swe1 = on_regex(r"woc|草|wc|艹|我超|卧槽|操|靠|wok|wk|离.*?谱|\?+")

@swe1.handle()
async def handle_reasy_group(event: GroupMessageEvent):
    if "CQ" in str(event.get_message()):
        return
    await Matcher.send(event.get_message())

@swe1.handle()
async def handle_reasy_private(event: PrivateMessageEvent):
    if "CQ" in str(event.get_message()):
        return
    await Matcher.send(event.get_message())

