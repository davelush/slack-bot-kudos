import logging
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['app'] = 'slack-bot-kudos'
        log_record['filename'] = '{}:{}'.format(record.filename, record.lineno)
        log_record['function'] = record.funcName
        log_record['level'] = record.levelname


def initialise_logging(log_level):
    logger = logging.getLogger()
    if log_level:
        logger.setLevel(log_level)
    else:
        logger.setLevel(logging.INFO)


def setup_loggers():
    logger = logging.getLogger()
    log_handler = logging.StreamHandler()
    formatter = CustomJsonFormatter('%(asctime)s %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
