import logging as log


class LogGen:
    @staticmethod
    def loggen():
        for handler in log.root.handlers[:]:
            log.root.removeHandler(handler)
        log.basicConfig(filename="C:/Users/xyz/PycharmProjects/nopcommerce_project/Logs/automation.log", filemode='w',
                        format="%(asctime)-12s %(levelname)s: %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
        logger = log.getLogger()
        logger.setLevel(log.INFO)
        return logger
