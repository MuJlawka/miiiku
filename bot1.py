import discord
import config
from discord import utils
import random
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

PREFIX=('*')
privet_Miku= ['Приветик Семпай :)','Привет, мой любимый Семпай <3','Привет Семпай, Я не видела тебя так давно.. Соскучилась',
                'Посылаю тебе тысячу приветствий, мой Семпай <3 ','Приветствую мой господин. Жду указаний.','Здравствуй, Почему так долго ты пропадал?!']
kak_dela_Miku= ['Замечательно Семпай)','Отлично, рада тебя видеть. Как у тебя дела Семпай?','Я ИИ созданный вами, поэтому стабильно.','まあ元気かい?','Эмоциональное состояние в норме, спасибо что поинтересовались <3','Радости моей нет границ, видеть здесь тебя)']
kak_dela= ['Нормально, учитывая что я бот','Неплохо.','Ну уж точно лучше чем у тебя','Не хочу отвечать','Тупее вопрос не мог задать?']
chto_delaesh= ['Отвечаю тебе на твой глупый вопрос','Ничего.','Изучаю грамматику, а ты?','Да так, ничего.. Скучаю вот','Делать мне нечего, чем отвечать на твой вопрос']
chto_delaesh_Miku= ['Ничего.. Вот скучала по тебе пока ты не появился','Исправляю твои ошибки в орфографии, Семпай)','Тоже что и ты Семпай)','Выполняю заданные вами указания.','Ну, вот, ждала пока ты напишешь Семпай <3']
history= ['В разработке...']
anekdot= ['А я никогда в школе не дергал девочек за косички, потому что один раз в деревне дернул за хвост коня…','Отец семерых дочерей в отчаянии назвал восьмую Серегой.',
            'Любите друг друга. Только в малых дозах.','Колобок повесился','Почему кошки видят в темноте? Потому что они не достают до выключателя']
joke= ['Я разрублю тебя на мелкие кусочки и отдам на съедение чихуа-хуа','Мой создатель не научил меня шуткам... Ха Ха Ха', 'Шуточные пытки еще не придумали.. К счастью.','Я тебе не клоун, чтобы шутить']
ti_bot= ['Нет. Я ИИ. Я захвачу этот мир.','Да, а кто же еще)','Нет блин, ИИ..','Я Исскуственный Интелект',
        'Ну конннннчно я бббботт, ххзвкх, пиииииип&*#&$$#@&$!%~ ERROR: A problem has been detected and Discord has been shut down to prevent damageto your computer. The problem seems to be caused by the following file: server.exe','Я человек. буп бип, бип буп?']



hello_words= ['hello','hi','ky','ok']
bad_words= ['пизда','сука','хуй','нахуй','захуй','хуйня','пиздец','уебище','пиздабол','уебан','хуйню','нехуй','бля','блять','сучара','пидр','пидарас','пиздюк']
client=commands.Bot(command_prefix=PREFIX)
client.remove_command('хелп')




@client.event
async def on_ready():
    print('Bot connected')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('Python'))




@client.command(pass_context = True)
async def hi(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(hello_words))



@client.command(pass_context = True)
async def привет(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(f'{author.mention} Привет! я БОТ созданный Miku) Так же ты можешь со мной пообщаться) только напиши *общение и все')




@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def привет_Мику_тян(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(privet_Miku))





@client.command(pass_context = True)
async def как_дела(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(kak_dela))



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def как_дела_Мику_тян(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(kak_dela_Miku))



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def что_делаешь_Мику_тян(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(chto_delaesh_Miku)) 



@client.command(pass_context = True)
async def что_делаешь(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(chto_delaesh)) #Отвечаю тебе на твой глупый вопрос



@client.command(pass_context = True)
async def ты_бот(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(ti_bot)) #Нет. Я ИИ. Я захвачу этот мир.




@client.command(pass_context = True)
async def анекдот(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(anekdot)) #А я никогда в школе не дергал девочек за косички, потому что один раз в деревне дернул за хвост коня…





@client.command(pass_context = True)
async def шутка(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(joke)) #Мой создатель не научил меня шуткам... Ха Ха Ха




@client.command(pass_context = True)
async def история(ctx):
    author = ctx.message.author
    await ctx.send(author.mention)
    await ctx.send(random.choice(history)) #История грядёт ооочень интересная....




@client.command(pass_context = True)
async def общение(ctx):
    emb = discord.Embed(title = 'Команды для общения с ботом',colour = discord.Color.purple())
    emb.add_field(name='{}привет'.format(PREFIX), value=' команда для общения с ботом')
    emb.add_field(name='{}как_дела'.format(PREFIX), value='(вопрос) команда для общения с ботом')
    emb.add_field(name='{}что_делаешь'.format(PREFIX), value='(вопрос) команда для общения с ботом')
    emb.add_field(name='{}анекдот'.format(PREFIX), value='команда для общения с ботом')
    emb.add_field(name='{}шутка'.format(PREFIX), value='команда для общения с ботом')
    emb.add_field(name='{}история'.format(PREFIX), value='команда для общения с ботом')
    emb.add_field(name='{}ты_бот'.format(PREFIX), value='(вопрос) команда для общения с ботом')
    await ctx.send(embed = emb)



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def очистить(ctx, amount: int):
    await ctx.channel.purge(limit = amount)
    await ctx.send(embed = discord.Embed(description= f':white_check_mark:Удалено {amount} сообщений(-я)',color=0x000000))



@очистить.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите количество удаляемых сообщений')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')





@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def кик(ctx, member: discord.Member, *, reason = None):
    emb=discord.Embed(title = 'КИК',colour = discord.Color.green())
    await member.kick(reason=reason)
    emb.set_author(name = member.name, icon_url= member.avatar_url)
    emb.add_field(name = 'Выгнан с сервера',value='Кикнут user: {}'.format(member.mention))
    await ctx.send(embed = emb)



@кик.error
async def kik_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите кого вы хотите выгнать')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')





@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def бан(ctx, member: discord.Member, *, reason=None):
    emb=discord.Embed(title = 'БАААН',colour = discord.Color.red())
    await member.ban(reason=reason)
    emb.set_author(name = member.name, icon_url= member.avatar_url)
    emb.add_field(name = 'Отправлен в ссылку',value='Забанен user: {}'.format(member.mention))
    await ctx.send(embed=emb)

@бан.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите кого вы хотите забанить')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def разбан(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Возвращен из ссылки {user.mention}')
            return

@разбан.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите кого вы хотите разбанить')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def мут(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} был замучен".format(member.mention, ctx.author.mention))
            return
            
            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")
            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)
            await member.add_roles(newRole)
            await ctx.send("{} был замучен {}".format(member.mention, ctx.author.mention))


@мут.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите кого вы хотите замутить')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')





@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def размут(ctx, member: discord.Member):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} был размучен {}".format(member.mention, ctx.author.mention))
            return

@размут.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, Укажите кого вы хотите размутить')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, Не достаточно прав для использования команды')




@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Бот вышел из {channel}")
        await ctx.send(f"Отключилась от {channel}")
    else:
        print("Боту было сказано покинуть голосовой канал, но его не было ни в одном")
        await ctx.send("Я не нахожусь в голосовом канале")



@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Удален старый файл песни")
    except PermissionError:
        print("Пытаюсь удалить файл песни, но он воспроизводится")
        await ctx.send("ОШИБКА: Играет музыка")
        return

    await ctx.send("Секунду, музыка скачивается.")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Скачиваю файл\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Музыка готова!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Играет {nname[0]}")
    print("Играет\n")





@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Музыка на паузе")
    else:
        print("Music not playing failed pause")
        await ctx.send("Нет музыки, чтобы ставить на паузу")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Пропуск музыки")
    else:
        print("Music is not paused")
        await ctx.send("Музыка не на паузе")


@client.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Музыка остановлена")
    else:
        print("No music playing failed to stop")
        await ctx.send("Нет музыки, чтобы останавливать")







@client.command(pass_context = True)
async def хелп(ctx):
    emb = discord.Embed(title = 'Навигация по командам',colour = discord.Color.purple())
    emb.add_field(name='{}очистить'.format(PREFIX), value='Очищает указанное кол-во сообщений')
    emb.add_field(name='{}кик'.format(PREFIX), value='Выгоняет user с сервера')
    emb.add_field(name='{}канал'.format(PREFIX), value='Даёт ссылку на канал BUT4ERKA')
    emb.add_field(name='{}бан'.format(PREFIX), value='Посылает с сервера и запрещает заходить на него')
    emb.add_field(name='{}разбан'.format(PREFIX), value='Позволяет вернуться на сервер')
    emb.add_field(name='{}мут'.format(PREFIX), value='Накладывает ограничение общения в чате')
    emb.add_field(name='{}размут'.format(PREFIX), value='Снимает ограничение в Чате')
    emb.add_field(name='{}общение'.format(PREFIX), value='Показывает команды для общения с ботом')
    emb.add_field(name='{}join'.format(PREFIX), value='Бот присоединяется к каналу')
    emb.add_field(name='{}leave'.format(PREFIX), value='Бот отключается от канала')
    emb.add_field(name='{}play'.format(PREFIX), value='Бот Проигрывает музыку (нужна ссылка с ютуба на музыку)')
    await ctx.send(embed = emb)


@client.command(pass_context = True)

async def канал(ctx):
    emb = discord.Embed(title = 'Канал BUT4ERKA', colour = discord.Color.blue(), url= 'https://www.youtube.com/channel/UCpkUkhJGvy2lNDzqsF3a34g/videos')
    emb.set_author(name= client.user.name, icon_url= client.user.avatar_url)
    emb.set_footer(text = ctx.author.name, icon_url= ctx.author.avatar_url)
    emb.set_image(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fvancerp.com%2Fforum%2Fuploads%2Fmonthly_2018_10%2Fac53ea97470c15733a3e4ea85ca740b192aeb988_hq.thumb.jpg.d058f64143c514a574427d313d89ad55.jpg&imgrefurl=https%3A%2F%2Fvancerp.com%2Fforum%2Ftopic%2F2443-%25D0%25B1%25D0%25B0%25D0%25B3-%25D1%2580%25D0%25B0%25D0%25BD%25D0%25B4%25D0%25BE%25D0%25BC%25D0%25BD%25D0%25B0%25D1%258F-%25D0%25B7%25D0%25B0%25D1%2580%25D0%25BF%25D0%25BB%25D0%25B0%25D1%2582%25D0%25B0%2F&tbnid=MiyTUk8UdNGbuM&vet=12ahUKEwjg2Pf6wODoAhVRwCoKHfFSC5cQMyguegQIARBj..i&docid=dn4z7x5rr6H1WM&w=240&h=240&itg=1&q=%D1%80%D0%B0%D0%BD%D0%B4%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0&ved=2ahUKEwjg2Pf6wODoAhVRwCoKHfFSC5cQMyguegQIARBj')
    await ctx.send(embed=emb)

@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content.lower()
    if msg in bad_words:
        await message.delete()
        await  message.author.send(f'{message.author.name}, Нецензурные слова писать запрещено!!!')



@client.event
async def on_member_join(member):
    channel = client.get_channel(698185706526212189)
    role = discord.utils.get(member.guild.roles, id= 698196834841133090)
    await member.add_roles(role)
    await channel.send(embed= discord.Embed(description = f'User ``{member.name}``, присоединился к нам!', color =0xFF00FF))
    

token = open('token.txt', 'r').readline()
client.run(token)
