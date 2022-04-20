from nonebot import require, get_bot


scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job("interval", seconds=5)
async def demo1():
    try:
        get_bot()
    except:
        print("bot未连接!!!")
        return