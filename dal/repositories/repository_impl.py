

from dal.models import Config as ConfigModel
from dal.entities.entity import GenenericEntity


'''
The StockRepository class acts as an intermediary between the 
application code and the database data mapping laters. Acting like an in-memory
collection of domain objects.It provides methods for 
retrieving, adding, updating, and deleting Stock entities in 
the database using the SQLAlchemy session. The methods make use 
of the data model class, which is defined in the models.py file, 
to interact with the underlying database table.
'''


class ConfigureRepository(GenenericEntity[ConfigModel]):
    def __init__(self, session):
        super().__init__(ConfigModel, session)
