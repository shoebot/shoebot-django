from StringIO import StringIO

import shoebot

XML_PREAMBLE = '<?xml version="1.0" encoding="UTF-8"?>'

def strip_preamble(buff):
    """
    :param buff: buffer with svg data

    Skip the preamble in the buffer then output the rest.
    """
    pass

def run_bot(filename, inline=True, **kwargs):
    """
    Run a named bot, and output SVG.
    """    
    buff = StringIO()
    bot = shoebot.bot(buff=buff, format="svg", **kwargs)
    bot.run(filename)

    if inline:
        buff.seek(len(XML_PREAMBLE))
    else:
        buff.seek(0)

    return buff.read()

