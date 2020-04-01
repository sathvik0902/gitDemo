import logging

def getLogger():

    logger = logging.getLogger(__name__)


    filehandler = logging.FileHandler("logfile.log")
    formeter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s :")
    filehandler.setFormatter(formeter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("Debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.critical("critical message")
    logger.error("error message")
