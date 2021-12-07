# Testing the GitHub API, using the Blender repo.
# Liam O Lionaird [19335530] - created 12 Dec 2021

from github import Github
import os
import json

# Acquiring my access token stored in an environment variable.
# You must replace this with your own access token to run the program.
git = Github(os.getenv("GIT_TOKEN"))

blend = git.get_repo("blender/blender")

print("Repo description:\n" + blend.description)