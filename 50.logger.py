import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(name)s - %(levelname)s-%(message)s')
logger = logging.getLogger(__name__) # se utiliza para asegurar que tenga un nombre unico basado en el modulo donde se encuentra
#logger.info("Este es un mensaje de informacion")
logger.debug("Este es un mensaje de depuracion")
logger.info("Este es un mensaje de informacion")
logger.warning("Este es un mensaje de advertencia")
logger.error("Este es un mensaje de error")
logger.critical("Este es un mensaje critico")