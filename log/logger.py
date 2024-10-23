import logging
from .collection_handler import CollectionHandler
logger = logging.getLogger("project1")
logger.setLevel(logging.INFO)
handler = CollectionHandler()
logger.addHandler(handler)