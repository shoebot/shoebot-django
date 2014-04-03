import os

# Using shoebot for server side graphics in django
# Remember bots are python code - be careful out
# there !

from django.shortcuts import render_to_response
from django.utils.html import mark_safe
from django.conf import settings

from djbot import run_bot

def bot(request):
    fn = os.path.join(settings.BASE_DIR, 'shoebot_demos/bots/flowers.bot')
    bot_svg = run_bot(fn)
    return render_to_response("bot.html", {'bot': mark_safe(bot_svg) })


