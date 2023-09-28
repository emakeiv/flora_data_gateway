from dal.repositories.repository_registry import RepositoryRegistry
from dal.repositories.repository_impl import ConfigureRepository
from app.server import create_server


repository_registry = RepositoryRegistry()
repository_registry.add('configure', ConfigureRepository)

app = create_server(repositories=repository_registry)
