from sqlalchemy import text, insert
from database import sync_engine, async_engine
from models import metadata_obj, workers_table


def get_123_sync():
    with async_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3 union SELECT 4, 5, 6"))
        print(f'{res.first()=}')

async def get_123_async():
    async with async_engine.connect() as conn:
      res = await conn.execute(text("SELECT 1, 2, 3 union SELECT 4, 5, 6"))
      print(f'{res.first()=}')

def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volk"}
            ]
        )
        conn.execute(stmt)
        conn.commit()
