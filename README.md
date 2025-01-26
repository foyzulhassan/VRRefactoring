# VR Refactoring
STEP-1: Create a vitual environment using the commands ``python -m venv venv``
STEP-2: Clone the repository from https://github.com/foyzulhassan/VRRefactoring.git 
STEP-3: Create a folder called Project_Repo on the root directory. This will store all the cloned repositories listed in the VR_Project_List.txt file.
STEP-4: configure your root directory, Project_Repo by creating them in the .env file.
STEP-5: Run the clone.py script.
STTEP-6: Wait until all the VR projects have been cloned into your enviroment under Project_Repo directory.
STEP-7: Run the Main.py script.
STEP-8: A file called commits_information.csv will be created and it will have all the details about the commits that have the search keyword(s). It will include the project name, commit message, commit id and commit url, respectively. 


# VR Projects

This repository contains tools and scripts designed for managing and analyzing VR-related repositories. The goal of this project is to clone various VR projects, traverse their commit history, and extract relevant data based on predefined criteria. This data is to be used to get a better understanding of refactoring in VR projects and reduce technical debt in VR software development.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Cloning Repositories](#cloning-repositories)
  - [Analyzing Commits](#analyzing-commits)
  - [Keywords for Commit Filtering](#keywords-for-commit-filtering)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Project Overview

The VR Projects tool automates the cloning and analysis of VR repositories. It uses Python scripts to traverse commit histories, extract relevant commit messages, and store useful information for further analysis.

## Features

- Clone VR repositories from a specified list of URLs.
- Traverse and analyze commit history using `pydriller`.
- Extract and filter commit messages based on specified keywords.
- Store relevant commit information in a CSV file for further processing.

## Requirements

The project relies on the following dependencies:

- Python 3.10 or above
- Git
- `pydriller` - A Python package to mine Git repositories
- `python-dotenv` - For loading environment variables
- `gitpython` (optional, if used)

To install the dependencies, use:

```bash
pip install -r requirements.txt

## Installation
Clone the repository:
git clone https://github.com/foyzulhassan/VRRefactoring.git 
cd VR Refactoring
Install the required Python packages as mentioned in the Requirements section.

## Usage
Cloning Repositories
The clone.py script handles cloning of repositories listed in a text file specified by the GIT_REPO_FILES environment variable.

## Analyzing Commits
The Main.py script traverses the commit history of cloned repositories and extracts relevant information based on a predefined list of keywords. The extracted data is saved in a CSV file.

## To execute:

python3 src/main/clone.py
python3 src/main/Main.py

## Keywords for Commit Filtering
The following keywords are used to filter commit messages:

refactor

## Configuration
Configuration
Environment variables are used to configure the project. Create a .env file in the root directory and add the following variables:

PROJECT_DIR=/path/to/your/project_directory/Project_Repo/
ROOT_DIR=/path/to/your/root_directory/
GIT_REPO_FILES=path/to/repo_list.txt

## Project Structure

```bash
VR_Refactoring/
├── src/
│   ├── main/
│   │   ├── clone.py        # Script for cloning repositories
│   │   ├── Main.py         # Main script for traversing and analyzing commits
│   │   └── utility.py      # Utility functions for extracting repository details
├── .env                    # Environment variables configuration
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation (this file)
└── VR_Project_list.txt     # Project list of VR documentation (this file)

## Contributing
Contributions are welcome! Please fork this repository and create a pull request with your proposed changes. For major changes, please open an issue first to discuss what you would like to change.



