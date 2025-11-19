from github import Github
from app.core.config import settings
import requests

class GitHubService:
    def __init__(self):
        self.client = Github(settings.GITHUB_TOKEN)

    def get_pr_diff(self, repo_name: str, pr_number: int) -> str:

        repo = self.client.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        

        response = requests.get(pr.diff_url, headers={"Authorization": f"token {settings.GITHUB_TOKEN}"})
        response.raise_for_status()
        return response.text

    def parse_diff(self, diff_text: str) -> list[dict]:

        files = []
        current_file = None
        current_lines = []
        
        for line in diff_text.split('\n'):
            if line.startswith('diff --git'):
                if current_file:
                    files.append({"file": current_file, "changes": "\n".join(current_lines)})
                current_file = line.split(' ')[-1].lstrip('b/')
                current_lines = []
            elif line.startswith('+++') or line.startswith('---') or line.startswith('index'):
                continue
            else:
                current_lines.append(line)
        
        if current_file:
            files.append({"file": current_file, "changes": "\n".join(current_lines)})
            
        return files

github_service = GitHubService()
