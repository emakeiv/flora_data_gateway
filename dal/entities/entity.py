from typing import TypeVar, List
from dal.entities.entity_interface import IEntity
from dal.entities.base_entity import BaseEntity
'''
bound property in TypeVar provides a way to specify a 
constraint on the type variable. When we set a bound, 
it means that the type variable must be a subclass of 
the bound type. In this context, we use Entity as a 
placeholder for a specific business entity class, and 
the bound=BaseEntity ensures that any type passed to 
Entity must be a subclass of BaseEntity. This constraint 
helps maintain type safety and prevents incorrect usage of
the EntityRepository with incompatible types.
'''

T = TypeVar("T", bound=BaseEntity)


class GenenericEntity(IEntity[T]):
    def __init__(self, entity, session):
        self.entity = entity
        self.session = session

    def get(self, symbol: str) -> T:
        return self.session.query(self.entity).filter_by(symbol=symbol).first()

    def list(self, offset: int = None, limit: int = None, **query_conditions) -> List[T]:
        query = self.session.query(self.entity)

        for key, value in query_conditions.items():
            query = query.filter(getattr(self.entity, key) == value)

        if offset is not None:
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)

        return [entity.dict() for entity in query.all()]

    def add(self, entity, **kwargs) -> T:
        entity_model = self.entity(**kwargs)
        self.session.add(entity_model)
        self.session.commit()
        return entity_model

    def update(self, entity_id: int, **kwargs) -> T:
        entity_model = self.session.query(
            self.entity).filter_by(id=entity_id).first()
        if entity_model:
            for key, value in kwargs.items():
                setattr(entity_model, key, value)
            return entity_model.dict()
        return None

    def delete(self, entity_id: int) -> None:
        entity_model = self.session.query(
            self.entity).filter_by(id=entity_id).first()
        if entity_model:
            self.session.delete(entity_model)
            self.session.commit()

    def bulk_insert(self, records: List[dict]) -> None:
        self.session.bulk_insert_mappings(self.entity, records)
        self.session.commit()
