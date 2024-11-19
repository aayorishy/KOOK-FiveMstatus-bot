from khl import Bot, Message
import aiohttp

bot = Bot(token='1/MzI0NjM=/2Ifzdd4kBC/+s5Ax6KhLfA==') # 请替换为你的Token

@bot.command(name="fivemol", case_sensitive=False)
async def fivemol(msg: Message):
    fivem_ip = "r8rrpg"  # 请替换为实际的服务器IP
    fivem_name = "test"  # 请替换为实际的服务器名称

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://servers-frontend.fivem.net/api/servers/single/{fivem_ip}') as resp:
            if resp.status != 200:
                return await msg.reply('无法获取服务器数据')

            data = await resp.json()
            server_data = data.get('Data', {})
            players = server_data.get('clients', 0)
            max_players = server_data.get('sv_maxclients', 0)

            status_text = "发生异常" if players == 0 else "正常运行"
            status_msg = f"**服务器名字**: {fivem_name}\n**服务器状态**: {status_text}\n**服务器人数**: \n{players}/{max_players}\n"
            await msg.reply(status_msg)

bot.run()