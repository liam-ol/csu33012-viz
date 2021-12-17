# Software Engineering Visualisation Project

**by Liam O Lionaird [19335530] for CSU33012 - Software Engineering.**

## Concept: *Big Tech Open Source: Employees vs. The World*

With the acquiring of Github by Microsoft, big tech's interest and investment in open-source development has been made loud and clear. But just how 'open' are big tech's new open-source project ventures? How much do outside contributors *actually* contribute in comparison to employees? This visualisation analyses contributors to a long-running and popular open-source project from Microsoft, [Visual Studio Code](https://github.com/microsoft/vscode). It compares employee contributions with outsider contributions, and presents the results.

## Implementation

### API

All contributors to the VS Code repo are available for easy access with the Github API, as well as their number of contributions. It is also possible to detect whether a user is a member of Microsoft's GitHub 'organisation' (i.e. whether they are an employee). 

The code sorts through each contributor, logging their number of contributions and their affiliation with Microsoft. It returns a JSON database with the following style: ``{name:(string), employee:(bool), contribs:(int)}``

Note that GitHub's API restricts the number of contributors it returns - currently it only shows the top 365 contributors.

### Visualisation

To be decided.