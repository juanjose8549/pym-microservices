from ..database.db_connection import engine

async def insert_advisor(Advisor):
    return await engine.save(Advisor)