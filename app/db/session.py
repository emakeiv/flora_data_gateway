from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine(
    'postgresql://postgres:superpass@localhost/flora_data_storage',
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10
)

LocalSession = sessionmaker(bind=engine)
