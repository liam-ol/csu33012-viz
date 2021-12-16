# My core visualisation code for the Software Engineering project.
# Liam O Lionaird [19335530]

from github import Github
import os
import json


# Acquiring my access token stored in an environment variable.
# You must replace this with your own access token to run the program.
git = Github(os.getenv("GIT_TOKEN"))
microsoft = git.get_organization("microsoft")
vscode = git.get_repo("microsoft/vscode")

# is_employee: Given a username string, return True if they are an employee of Microsoft.
def is_employee(user):
    # Usually an employee is a member of Microsoft's GitHub 'organisation'.
    # Sometimes they are not, but have 'Microsoft' listed as their 'company' on their user page.
    if microsoft.has_in_members(git.get_user(user)) or "microsoft" in git.get_user(user).company.lower():
        return True
    else:
        return False

# process_user: Given an entry in the repo's contributors list, process it into a database entry.
def process_user(contributor):
    # Gather data from contributor.
    name = contributor.login
    employed = is_employee(name)
    contribs = contributor.contributions
    # Pack this data into a dictionary.
    userdict = {"name": name, "employed": employed, "contribs": contribs}
    # Convert this dict to a json object.
    return json.dumps(userdict)

# TODO: FUNCTION TO CREATE JSON DATABASE
# def write_database():
