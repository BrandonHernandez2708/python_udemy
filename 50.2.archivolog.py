import logging
logging.basicConfig(filename="mi_registro.log",
level=logging.DEBUG, format='%(asctime)s - %(name)s - %(name)s - %(levelname)s-%(message)s')
logger = logging.getLogger(__name__)
logger.debug("Este se guardara en archivo")
logger.info("Este se guardara en archivo")