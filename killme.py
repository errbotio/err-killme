from errbot import botcmd, BotPlugin
import logging
import os
import signal

log = logging.getLogger(__name__)

class KillMe(BotPlugin):
    @botcmd(admin_only=True)
    def killme(self, mess, args):
        os.kill(os.getpid(), signal.SIGTERM)

