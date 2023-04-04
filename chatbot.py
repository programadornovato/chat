from rivescript import RiveScript

bot = RiveScript()
bot.load_file('ejemplo.rive')
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot> ' + str(reply))
