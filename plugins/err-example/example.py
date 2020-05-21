from errbot import BotPlugin, botcmd
import json


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.%
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It *works* !'  # This string format is markdown.

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world."""
        return "Hello, world!"

    @botcmd
    def quellcode(self, msg, args):
        return 'Hallo! Der Quellcode ist auf [Github](https://github.com/pgrunm/FOM-Errbot) zu finden.'

    @botcmd
    def reverse(self, msg, args):
        return args[::-1]
