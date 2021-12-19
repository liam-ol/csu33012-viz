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
    if microsoft.has_in_members(git.get_user(user)):
        return True
    elif git.get_user(user).company is not None:
        return "microsoft" in git.get_user(user).company.lower()
    else:
        return False

# process_user: Given an entry in the repo's contributors list, process data and return a dictionary.
def process_user(contributor):
    # Names are no longer returned to preserve anonymity.
    return {"employed": is_employee(contributor.login),
            "contribs": contributor.contributions}

# write_database: Given a list of contributors, write a JSON database file we can use.
def write_database():
    # Track number of users processed.
    total_users = vscode.get_contributors().totalCount
    user_list = []
    # First compose a list of contributor dicts.
    for user in vscode.get_contributors():
        user_list.append(process_user(user))
        print(f"[{len(user_list)}/{total_users}]  User {user.login} processed.")
    database = {"database": user_list}
    # Write into "db.js". (Creates if it doesn't exist + automatically clears file.)
    # We must convert this database to a JavaScript file for use with our visualisation.
    db = open("db.js", "w")
    db.write("var db = ")
    db.write(json.dumps(database, indent=2))


write_database()    # <- Comment this when running tests, unless you want to be here all day.
