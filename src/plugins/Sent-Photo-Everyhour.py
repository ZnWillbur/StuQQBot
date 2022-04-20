from nonebot import require, get_bot
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment


scheduler = require('nonebot_plugin_apscheduler').scheduler

def tempelate(hour):
    try:
        bot = get_bot()
    except:
        print(f"{hour}时,发送图片失败!!")
        return
    group_id=809011943
    message = Message([
    MessageSegment(type='image', data={'file':f'https://mengxingheng.xyz/Timg/{hour}.jpg'})])
    return bot, group_id, message

@scheduler.scheduled_job("cron", hour=6, minute=0)
async def demo6():
    bot, group_id, message= tempelate(6)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=7, minute=0)
async def demo7():
    bot, group_id, message= tempelate(7)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=8, minute=0)
async def demo8():
    bot, group_id, message= tempelate(8)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=9, minute=0)
async def demo9():
    bot, group_id, message= tempelate(9)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=10, minute=0)
async def demo10():
    bot, group_id, message= tempelate(10)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=11, minute=0)
async def demo11():
    bot, group_id, message= tempelate(11)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=12, minute=0)
async def demo12():
    bot, group_id, message= tempelate(12)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=13, minute=0)
async def demo13():
    bot, group_id, message= tempelate(1)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=14, minute=0)
async def demo14():
    bot, group_id, message= tempelate(2)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=15, minute=0)
async def demo15():
    bot, group_id, message= tempelate(3)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=16, minute=0)
async def demo16():
    bot, group_id, message= tempelate(4)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=17, minute=0)
async def demo17():
    bot, group_id, message= tempelate(5)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=18, minute=0)
async def demo18():
    bot, group_id, message= tempelate(6)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=19, minute=0)
async def demo19():
    bot, group_id, message= tempelate(7)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=20, minute=0)
async def demo20():
    bot, group_id, message= tempelate(8)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=21, minute=0)
async def demo21():
    bot, group_id, message= tempelate(9)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=22, minute=0)
async def demo22():
    bot, group_id, message= tempelate(10)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=23, minute=0)
async def demo23():
    bot, group_id, message= tempelate(11)
    await bot.send_group_msg(group_id=group_id, message=message)

@scheduler.scheduled_job("cron", hour=0, minute=0)
async def demo0():
    bot, group_id, message= tempelate(12)
    await bot.send_group_msg(group_id=group_id, message=message)