import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')


@bot.command()
async def commands(ctx):
    await ctx.send('''
🌱 **COMANDOS DO ECOBOT**

🌎 `$hello` → Dá oi e apresenta o bot
♻️ `$dica` → Mostra uma dica ecológica
💡 `$ideia` → Dá uma ideia para reduzir o desperdício
🌳 `$frase` → Mostra uma frase sobre o meio ambiente
🎲 `$desafio` → Gera um desafio ecológico
🗑️ `$reciclagem` → Explica como descartar um material
😂 `$emoji` → Gera um emoji relacionado ao meio ambiente
❓ `$commands` → Exibe a lista de comandos
''')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! 🌱 Eu sou o {bot.user}, seu bot de sustentabilidade!')


@bot.command()
async def dica(ctx):
    dicas = [
        "Apague as luzes quando sair de um cômodo. 💡",
        "Feche a torneira enquanto escova os dentes. 🚰",
        "Prefira garrafas reutilizáveis em vez de garrafas descartáveis. 🥤",
        "Use sacolas reutilizáveis ao fazer compras. 🛍️",
        "Sempre que possível, prefira caminhar ou andar de bicicleta. 🚲",
        "Evite comprar mais comida do que você realmente precisa. 🍎",
        "Reutilize potes e embalagens antes de descartá-los. ♻️"
    ]

    resultado = random.choice(dicas)
    await ctx.send("🌱 **Dica ecológica:** " + resultado)


@bot.command()
async def ideia(ctx):
    ideias = [
        "Transforme potes de vidro em recipientes para guardar alimentos.",
        "Use folhas de papel dos dois lados antes de reciclá-las.",
        "Doe roupas que você não usa mais em vez de jogá-las fora.",
        "Faça uma composteira para aproveitar restos de alimentos.",
        "Conserte objetos quebrados antes de comprar novos.",
        "Use uma caneca reutilizável para evitar copos descartáveis."
    ]

    resultado = random.choice(ideias)
    await ctx.send("💡 **Ideia para reduzir o desperdício:** " + resultado)


@bot.command()
async def frase(ctx):
    frases = [
        "🌎 Pequenas atitudes podem gerar grandes mudanças.",
        "🌱 Cuidar do planeta também é cuidar do nosso futuro.",
        "♻️ Antes de jogar fora, pense se esse objeto pode ser reutilizado.",
        "🌳 A natureza não precisa de pessoas perfeitas, mas de pessoas que façam a sua parte.",
        "💚 O futuro depende das escolhas que fazemos hoje."
    ]

    resultado = random.choice(frases)
    await ctx.send(resultado)


@bot.command()
async def desafio(ctx):
    desafios = [
        "Passe o dia sem usar copos descartáveis! 🥤",
        "Hoje, tente economizar água durante o banho! 🚿",
        "Separe corretamente o lixo reciclável da sua casa! ♻️",
        "Passe um dia evitando desperdício de comida! 🍎",
        "Se possível, caminhe ou use bicicleta em um trajeto curto! 🚲",
        "Reutilize algum objeto que seria jogado fora! 🔄"
    ]

    resultado = random.choice(desafios)
    await ctx.send("🎯 **Seu desafio ecológico:** " + resultado)


@bot.command()
async def reciclagem(ctx, material):
    materiais = {
        "papel": "📄 O papel limpo e seco pode ser separado para a reciclagem.",
        "plastico": "🥤 Plásticos recicláveis devem estar, de preferência, limpos antes do descarte.",
        "vidro": "🍾 Vidros podem ser reciclados, mas devem ser descartados com cuidado.",
        "metal": "🥫 Latas de alumínio e outros metais podem ser encaminhados para reciclagem.",
        "organico": "🍎 Restos de alimentos podem ser compostados quando houver essa possibilidade."
    }

    if material.lower() in materiais:
        await ctx.send(materiais[material.lower()])
    else:
        await ctx.send("❓ Não conheço esse material. Tente: papel, plastico, vidro, metal ou organico.")


@bot.command()
async def emoji(ctx):
    emojis = ["🌎", "🌱", "🌳", "♻️", "🌻", "🍃", "💚", "🌿", "🐝", "🌊"]

    resultado = random.choice(emojis)
    await ctx.send(resultado)


bot.run('SEU_TOKEN_AQUI')
