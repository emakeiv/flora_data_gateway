from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

T = TypeVar('T')


class IEntity(Generic[T]):
    @abstractmethod
    def get(self, entity_id: int):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity_id: int, entity):
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        pass
