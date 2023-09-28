from dataclasses import dataclass


@dataclass
class BaseEntity:
    def dict(self) -> dict:
        return {
            field.name: getattr(self, field.name) for field in self.__dataclass_fields__.values()
        }
