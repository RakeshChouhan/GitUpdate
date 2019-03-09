
from github import Github

class ProcessGit():
    user = ""
    password = ""
    def __init__(self):
        super().__init__()

    def start_git(self,user,password):
        self.user = user
        self.password = password
        g = Github(user, password)
        repos = g.get_user().get_repos()
        #for repo in repos:
           # self.process_repo(repo)
        return repos

    def process_repo(repo):
        print(repo.name)
        print(repo.git_url)
        print(repo.pulls_url)


