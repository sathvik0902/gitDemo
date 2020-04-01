import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler("logfile.log")
        formeter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s :")
        filehandler.setFormatter(formeter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger