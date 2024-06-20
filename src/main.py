#from queries.core import create_tables, insert_data
from queries.core import SyncCore
from queries.orm import SyncORM, AsyncORM
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
#SyncORM.select_workers_with_lazy_relationship()
#SyncORM.select_workers_with_joined_relationship()
#SyncORM.select_workers_with_selectin_relationship

async def main():
    await AsyncORM.insert_additional_resumes()

asyncio.run(main())

#async def main():
    #await AsyncORM.join_cte_subquery_window_func()
#asyncio.run(main())


