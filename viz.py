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

# process_user: Given an entry in the repo's contributors list, process data and return a JSON database object.
def process_user(contributor):
    # Gather data from contributor.
    name = contributor.login
    employed = is_employee(name)
    contribs = contributor.contributions
    # Pack this data into a dictionary.
    userdict = {"name": name, "employed": employed, "contribs": contribs}
    # Convert this dict to a JSON object.
    return json.dumps(userdict)

# write_database: Given a list of contributors, write a JSON database file we can use.
def write_database():
    # Writes into "db.json". (Creates if it doesn't exist.) Automatically clears file.
    db = open("db.json", "w")

    user_count = 0
    total_users = vscode.get_contributors().totalCount
    for user in vscode.get_contributors():
        db.write(process_user(user) + '\n')
        user_count += 1
        print(f"[{user_count}/{total_users}]  User {user.login} processed.")

write_database()