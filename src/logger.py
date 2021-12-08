import logging

METHOD = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
logging.basicConfig(filename='record.log', filemode='a',
                    level=logging.DEBUG, format=METHOD)
logger = logging.getLogger(__name__)


def get_logger():
    try:
        return logger
    except Exception as e:
        print("EXCEPTION SETTING LOGGER: ", e)
        raise e
