from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

import discord
from discord.ext import commands

curSet = Card.where(set="otj", number=4)
i = 0
for card in curSet.all():
    print(card.name)
    i += 1
print(i)

