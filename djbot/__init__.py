from django.conf import settings
from StringIO import StringIO

import shoebot

XML_PREAMBLE_LENGTH = len('<?xml version="1.0" encoding="UTF-8"?>')

def bot_allowed(bot_path):
    """
    A bot must be in the setting ALLOWED_BOTS
    otherwise it will not run.

    :param bot_path: full path to bot
    :return: True if the bot is allowed to run.
    """
    return bot_path in getattr(settings, 'SHOEBOT_ALLOWED_BOTS', [])


def render_bot(filename, inline=False, format='svg', **kwargs):
    """
    Run a named bot, and output SVG.

    :param inline: If True Output SVG with no XML preamble (suitable for mixing with HTML).
    """

    if not bot_allowed(filename):
        raise Exception("Sorry this bot is not on the allowed list")
    
    buff = StringIO()
    bot = shoebot.create_bot(buff=buff, **kwargs)
    bot.run(filename)

    if inline:
        buff.seek(XML_PREAMBLE_LENGTH)
    else:
        buff.seek(0)

    return buff.read()


