#Author Name: Faraz Gurramkonda

import csv
import re
from cmath import e

import pydriller
import os

from pydriller import Repository
from git.exc import InvalidGitRepositoryError

import clone
from dotenv import load_dotenv

import utility
from utility import extract_details

def clone_reps(result, project_dir, csv_file_path):
    for res_link in result:
        owner_name, project_name = utility.extract_details(res_link)
        repo_directory = project_dir + f"{owner_name}/{project_name}"
        print("Repo directory -> traversed: ", repo_directory)
        try:
            for commit in Repository(repo_directory).traverse_commits():
                commit_id = commit.hash
                commit_message = commit.msg

                # Construct commit URL
                commit_url = f"https://github.com/{owner_name}/{project_name}/commit/{commit_id}"

                # Extract modified files
                modified_files = []
                if hasattr(commit, "modifications"):
                    modified_files = [mod.filename for mod in commit.modifications]
                elif hasattr(commit, "modified_files"):
                    modified_files = [mod.filename for mod in commit.modified_files]

                # Skip commits with more than 20 modified files
                if len(modified_files) > 20:
                    continue

                commit_search_list = ["refactor"]
                for search_keyword in commit_search_list:
                    # Use regex for "refactor*" to match patterns like "refactor", "refactored", etc.
                    if re.search(rf"{search_keyword}.*", commit_message, re.IGNORECASE):
                        data = [
                            project_name,
                            commit_message,
                            commit_id,
                            ", ".join(modified_files),  # Join modified file names into a single string
                            commit_url
                        ]
                        with open(csv_file_path, 'a') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(data)
        except Exception as e:
            print(f"An error occurred with repository {repo_directory}: {e}")
    print("Data appended to the CSV file {}".format(csv_file_path))

if __name__ == "__main__":
    load_dotenv()
    project_dir = os.getenv('PROJECT_DIR')
    root = os.getenv('ROOT_DIR')
    git_repo_file = os.getenv('GIT_REPO_FILES')
    path = root + git_repo_file
    repo = []
    csv_file_path = project_dir + 'commit_information.csv'
    result = utility.repo_collection(path, repo)
    clone_reps(result, project_dir, csv_file_path)
