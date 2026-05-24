import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name="my_logger", log_file="application.log", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

# Example usage
if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger is set up and ready to go!")
    log.warning("This is a warning message.")
    log.error("This is an error message!")
