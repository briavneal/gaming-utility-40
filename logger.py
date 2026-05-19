import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_FILE = 'game_utility.log'
LOG_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 3


def setup_logger(name):
    handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

# Example usage:
if __name__ == '__main__':
    logger = setup_logger('game_logger')
    logger.info('Logger setup complete. Ready to log!')