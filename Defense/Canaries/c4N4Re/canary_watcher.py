from emailer import Emailer

from psutil import cpu_percent
from psutil import virtual_memory
from psutil import net_connections

from time import sleep

class CanaryWatcher:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def _cpu(self):
        pass
    
    def _ram(self):
        pass
    
    def _disk(self):
        pass

    def _connections():
        pass

    def _files():
        pass

    def _startup():
        """
        Allow user in config.ini to specify what exectuables should be present
        in the startup registry entry. If a new entry appears, send email.
        """
        pass

    def watch(self):
        pass

    def send_alert(self):
        server  = self.config["smtp_server"]["server"]
        port    = self.config["smtp_config"]["port"]

        with Emailer(server, port) as email:
            pass

