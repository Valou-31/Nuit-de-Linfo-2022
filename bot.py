import interactions

from bd import BD

# Insérez dans les guillement votre token du bot discord
bot = interactions.Client(token="")

laBD = BD('databases/bd.sqlite')

@bot.event
async def on_ready():
    print("> Bot is ready!")

@bot.command(
    name="add_channel",
    description="ajouter un Channel",
    options = [
        interactions.Option(
            name="chan",
            description="Nom du nouveau channel",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def add_channel(ctx: interactions.CommandContext, chan: str):
    laBD.addChannel(chan)
    await ctx.send(f"> channel ajouté")

@bot.command(
    name="list_channel",
    description="lister les channels actifs"
)
async def list_channel(ctx: interactions.CommandContext):
    cont = "> liste des Channels :\n ```"
    for chan, id in laBD.getChannels():
        cont += f"{id:3} - {chan}\n"
    cont += "```"
    await ctx.send(cont)

@bot.command(
    name="del_channel",
    description="suprimmer un Channel",
    options = [
        interactions.Option(
            name="chan_id",
            description="id du channel",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def del_channel(ctx: interactions.CommandContext, chan_id: int):
    laBD.delChannel(chan_id)
    await ctx.send(f"> channel suprimmé")

@bot.command(
    name="add_message",
    description="ajouter un message",
    options = [
        interactions.Option(
            name="chan_id",
            description="id du channel",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="message_content",
            description="contenue du message",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def del_channel(ctx: interactions.CommandContext, chan_id: int, message_content: str):
    laBD.addMessage(message_content,chan_id)
    await ctx.send(f"> message ajouté")

@bot.command(
    name="list_message",
    description="lister les messages d'un channel",
    options = [
        interactions.Option(
            name="chan_id",
            description="id du channel",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="max_msg",
            description="nombre max de message",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def list_message(ctx: interactions.CommandContext, chan_id: int, max_msg: int):
    cont = f"> liste des Messages(max:{max_msg}) du channel {chan_id} :\n ```"
    for m, id in laBD.getMessages(chan_id, max_msg):
        cont += f"{id:3} - {m}\n"
    cont += "```"
    await ctx.send(cont)

@bot.command(
    name="del_message",
    description="suprimer les messages d'un channel",
    options = [
        interactions.Option(
            name="msg_id",
            description="id du channel",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def del_message(ctx: interactions.CommandContext, msg_id: int):
    laBD.delMessage(msg_id)
    await ctx.send(f"> message suprimmé")

bot.start()