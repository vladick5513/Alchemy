#from queries.core import create_tables, insert_data
from queries.orm import create_tables, insert_data
import asyncio

create_tables()
#asyncio.run(insert_data())

