import logging
from datetime import datetime
from database import DBManager

class CollectionHandler(logging.Handler):
    def __init__(self, level: int | str = 0) -> None:
        super().__init__(level)
        self.collection = DBManager.get_db().log
    
    def emit(self, record: logging.LogRecord) -> None:
        self.collection.insert_one({"timestamp": datetime.fromtimestamp(record.created), "message": record.getMessage()})
        