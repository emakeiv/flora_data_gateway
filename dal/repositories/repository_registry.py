
class RepositoryRegistry:
    def __init__(self):
        self.repositories = {}

    def add(self, repo_name, repo_class):
        if repo_name in self.repositories:
            raise ValueError(f"'{repo_name}' already is in the registry.")
        self.repositories[repo_name] = repo_class

    def get(self, repo_name):
        if repo_name not in self.repositories:
            raise ValueError(f"'{repo_name}' not found in the registry.")
        return self.repositories[repo_name]
