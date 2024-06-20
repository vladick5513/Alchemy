from sqlalchemy import text, insert, select, update
from database import sync_engine, async_engine
from models import metadata_obj, workers_table

#
#def get_123_sync():
    #with async_engine.connect() as conn:
        #res = conn.execute(text("SELECT 1, 2, 3 union SELECT 4, 5, 6"))
        #print(f'{res.first()=}')

#async def get_123_async():
    #async with async_engine.connect() as conn:
      #res = await conn.execute(text("SELECT 1, 2, 3 union SELECT 4, 5, 6"))
      #print(f'{res.first()=}')

class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table) # SELECT * FROM workers
            result = conn.execute(query)
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = "Misha"):
        with sync_engine.connect() as conn:
            #stmt = text("UPDATE workers SET username=:username WHERE id=:id")
            #stmt = stmt.bindparams(username=new_username, id=worker_id)
            stmt = (
                update(workers_table)
                .values(username=new_username)
                #.where(workers_table.c.id==worker_id)
                .filter_by(id=worker_id)
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def insert_resumes():
        with sync_engine.connect() as conn:
            resumes = [
                {"title": "Python Junior Developer", "compensation": 50000, "workload": Workload.fulltime,
                 "worker_id": 1},
                {"title": "Python Разработчик", "compensation": 150000, "workload": Workload.fulltime, "worker_id": 1},
                {"title": "Python Data Engineer", "compensation": 250000, "workload": Workload.parttime,
                 "worker_id": 2},
                {"title": "Data Scientist", "compensation": 300000, "workload": Workload.fulltime, "worker_id": 2},
            ]
            stmt = insert(resumes_table).values(resumes)
            conn.execute(stmt)
            conn.commit()



