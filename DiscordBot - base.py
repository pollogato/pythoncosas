# link para crear token del bot y crear el bot
# pueden poner un nombre al bot, cambiar su imagen, etc
# https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications


# Invitar bot al servidor
# cambiar lo que dice CLIENTID por el código del bot
# (el código del bot es ese número largo de entre 15 y 20 números de largo)
# https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=8


from discord.ui import Button, View
from discord import app_commands
from discord.ext import commands
import discord

# Documentación del módulo discord.py:
# (en caso que quieran saber más, pero no es necesario para este trabajo además de lo explicado en este código)
# https://discordpy.readthedocs.io/en/stable/index.html

# Llave de acceso al bot (token), se obtiene de la pagina del bot, (dónde lo crearon)
# deben poner la clave entre las comillas
keyBot = ""

# permite todos los intents
intents = discord.Intents.all()

# Se crea el objeto Bot, poner en las comillas el prefix que usarán
bot = commands.Bot(command_prefix="",intents=intents)

# Creando el comando 'hi'
@bot.command()
async def hi(ctx):
    # Esta función se activará solo si se usa el prefix seguido de 'hi'
    # en alguno de los canales que el bot puede ver
    await ctx.send("Hello Nurse...")





@bot.event
async def on_message(message):
    print(message.author.name,message.content ) #printe del autor del mensaje y su contenido
    # Esta funcion se activa cada vez que alguien envia un mensaje
    # a un canal que el bot pueda ver


    # Si el mensaje no es de este bot
    # para ignorar mensajes de este bot
    # ya que no queremos que el bot se responda a si mismo
    # y se descontrole en un ciclo infinito de respuestas    
    if message.author != bot.user:


        # contenido del mensaje que se envio al canal (texto)
        mensaje = message.content 

        # nombre del autor del mensaje
        autor = message.author.name
        
        # usar esta variable les permitirá etiquetar al autor del mensaje original
        # En python se vera una combinación del caracter @ y numeros que identifican al usuario
        # pero en discord se ve como una mension al usuario que envio el mensaje
        citar_autor = message.author.mention

        # int que identifica a los usuarios de Discord (es único para cada cuenta de Discord)
        autor_ID = message.author.id

        # este print solo aparece en python, no en discord
        # usen print para corroborar que lo que quieren hacer esté bien
        # antes de enviar el mensaje al servidor
        print(autor+": "+mensaje)


        # Si el mensaje es 'hi'
        if message.content == "hi": 

            # enviar al mismo canal de este mensaje el texto "hello world..."
            # el contenido dentro los parentesis debe ser un unico string
            await message.channel.send("hello "+ citar_autor)

            # enviar al autor un DM
            # el contenido dentro los parentesis debe ser un unico string
            await message.author.send("ON Mensaje privado para "+ message.author.name)

    #La siguiente línea debe ir al final de esta función para que además de ver el mensaje compruebe si es un comando específico del bot
    await bot.process_commands(message)#Ahora que vea si es un comando lo que se envió


    
    # Todo el codigo del bot debe estar dentro de la funcion on_message o en una función de comando
    # Sino no se ejecutara, ya que son las funciones que se activan al escuchar
    # un mensaje del servidor

# Instruccion que activa al bot con el token antes indicado
bot.run(keyBot)
