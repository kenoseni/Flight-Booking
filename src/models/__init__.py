"""Models"""

# Third Party Library
from sqlalchemy import event
from src.utilities.helpers import unique_uuid_generator

from .user import User

# associate the "before_insert" listener function with models
tables = [User]

for table in tables:
    event.listen(table, 'before_insert', unique_uuid_generator)
