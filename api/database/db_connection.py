from odmantic import AIOEngine, Model, ObjectId
import asyncio
from os import getenv
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(f'mongodb+srv://{getenv("MONGO_USERNAME")}:{getenv("MONGO_PASSWORD")}@{getenv("MONGO_HOSTNAME")}/?retryWrites=true&w=majority&appName={getenv("MONGO_CLUSTER")}')

engine = AIOEngine(client=client, database="advisors")