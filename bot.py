import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def commands(ctx):
    await ctx.send('''
📜 **COMANDOS DO LINDOLFO**

👋 `$hello` → Dá oi e se apresenta pra você
🎲 `$roll NdN` → Rola dados
😂 `$heh N` → Dá risada conforme o número de vezes solicitado
😀 `$emoji` → Gera um emoji aleatório
💬 `$phrases` → Exibe uma frase para te fazer refletir
❓ `$commands` → Exibe a lista de comandos
''')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá ! eu sou o bot {bot.user}!')

#easteregg
@bot.command()
async def manu(ctx):
    await ctx.send(f'Eu te amo! 💕')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def emoji(ctx):
    emojis = ["😀", "😂", "😎", "🤩", "🥳", "😈", "🤖", "👻", "🔥", "💀"]
    resultado = random.choice(emojis)
    await ctx.send(resultado)

@bot.command()
async def phrases(ctx):
    phrases = ["Seja a sua melhor versão!", "Você não precisa provar nada para quem torce contra você.", "O silêncio também é resposta. Nem tudo merece uma explicação.", "Viva a vida, não sabemos o dia de amanhã!", "Quem conhece o próprio valor, jamais implora por validação.", "A vida é feita de escolhas, e cada escolha tem uma consequência.", "Não desista, grandes coisas levam tempo.", "Acredite em você e tudo será possível.", "A felicidade não é um destino, é uma jornada.", "O sucesso é a soma de pequenos esforços repetidos dia após dia.", "Se seu jardim não está crescendo, é porque toda vez que uma flor nasce, você a arranca para mostrar aos outros que é um jardineiro."]
    resultado = random.choice(phrases)
    await ctx.send(resultado)

bot.run("Token Aqui!")
