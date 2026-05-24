import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_log.log', max_bytes=5*1024*1024, backup_count=3):
    # Create the logger
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler with rotation
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Usage example:
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger has been set up successfully!')
    logger.debug('This is a debug message.')
    logger.warning('This is a warning message.')
