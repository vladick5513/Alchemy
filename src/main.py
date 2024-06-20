#from queries.core import create_tables, insert_data
from queries.core import SyncCore
from queries.orm import SyncORM
import asyncio

SyncORM.create_tables()
#SyncCore.create_tables()

SyncORM.insert_workers()
#SyncCore.insert_workers()

#SyncCore.select_workers()
#SyncCore.update_worker()

SyncORM.select_workers()
SyncORM.update_worker()
SyncORM.insert_resumes()
SyncORM.select_resumes_avg_compensation()

