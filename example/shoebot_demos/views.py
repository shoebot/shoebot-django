import os

# Using shoebot for server side graphics in django
# Remember bots are python code - be careful out
# there !

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.html import mark_safe
from django.conf import settings

from djbot import render_bot

BOT_DIR = os.path.join(settings.BASE_DIR, 'shoebot_demos', 'bots')

bot_fn = os.path.join(settings.BASE_DIR, 'shoebot_demos/bots/flowers.bot')

def bot(request, filename, format="svg"):
    bot_path = os.path.join(BOT_DIR, "%s.bot" % os.path.splitext(filename)[0])
    
    if not os.path.isfile(bot_path):
        raise Exception("%s is not a bot file" % bot_path)

    bot_svg = render_bot(bot_path)
    return HttpResponse(bot_svg, content_type="image/svg+xml")

def index(request):
    bot_svg = render_bot(bot_fn, inline=True)
    return render_to_response("bot.html", {'bot': mark_safe(bot_svg) })


