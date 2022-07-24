from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot import on_startswith
from nonebot.matcher import Matcher
from nonebot.adapters import Message

swe1 = on_startswith("/")

@swe1.handle()
async def handle_first_receive(event: GroupMessageEvent):
    count = 0
    str1 = ""
    str2 = ""
    for i in event.get_message():
        if count == 0:
            string = str(i).strip("/").strip(" ").split(" ")
            print(string)
            if len(string) == 1:
                str1 = string[0]
            else:
                str1, str2 = string[:2]
            count += 1
        elif count == 1:
            i = str(i)
            if "at" in i:
                dest_qqnum = i.split("=")[-1].strip("]")
                host_qqnum = event.get_user_id()
                message = Message([
                MessageSegment(type='at', data={'qq':host_qqnum}),
                MessageSegment(type='text', data={'text':f'{str1} '}),
                MessageSegment(type='at', data={'qq':dest_qqnum}),
                MessageSegment(type='text', data={'text':f'{str2}!'}),])
                await Matcher.send(message)

