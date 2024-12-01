
import colorlog
import logging

class ANSIColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[36m',        # Cyan
        'INFO': '\033[34m',         # Blue
        'WARNING': '\033[33m',      # Yellow
        'ERROR': '\033[31m',        # Red
        'CRITICAL': '\033[1;31m',   # Bold Red
        'RESET': '\033[0m'          # Reset
    }

    def format(self, record):
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{record.levelname}{self.COLORS['RESET']}"
            record.msg = f"{self.COLORS[levelname]}{record.msg}{self.COLORS['RESET']}"
        return super().format(record)