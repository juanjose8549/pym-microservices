from ..database.db_connection import engine

async def get_all_advisors(Advisor):
    return await engine.find(Advisor)