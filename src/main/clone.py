#Author Name: Faraz Gurramkonda

import os
from dotenv import load_dotenv
import subprocess
import utility

def clone_repo(result,project_dir):
    for res_link in result:
        owner_name, project_name = utility.extract_details(res_link)
        repo_directory = os.path.join(project_dir, f"{owner_name}/{project_name}")
        # if os.path.exists(repo_directory):
        #     print(f"Skipping {repo_directory}, already exists.")
        #     continue
        os.makedirs(repo_directory, exist_ok=True)
        # Cloning the repository
        clone_command = f"git clone \"{res_link}\" \"{repo_directory}\""
        # if not os.path.exists(repo_directory):
        #     print("entered here")
        subprocess.run(clone_command, shell=True)
        # else:
        #     print(f"Skipping {repo_directory}, already exists.")


if __name__ == "__main__":
    load_dotenv()
    project_dir = os.getenv('PROJECT_DIR')
    root = os.getenv('ROOT_DIR')
    git_repo_file = os.getenv('GIT_REPO_FILES')
    path = root+git_repo_file
    repo = []
    result = utility.repo_collection(path, repo)
    clone_repo(result,project_dir)
    print("Downloading is Done")