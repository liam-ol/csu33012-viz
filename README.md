# Software Engineering Visualisation Project

**by Liam O Lionaird [19335530] for CSU33012 - Software Engineering.**

## [View here!](https://liam-ol.github.io/csu33012-viz/)

## Concept: *Big Tech Open Source: Employees vs. The World*

With the acquiring of Github by Microsoft, coupled with many other corporate ventures into open-source development, big tech's interest and investment in free and open software engineering has been strongly established in the wider world of the discipline.

But just how 'open' are big tech's new open-source projects? How much do outside contributors *actually* contribute in comparison to employees?

This visualisation analyses contributors to a long-popular open-source software from Microsoft, [Visual Studio Code](https://github.com/microsoft/vscode). It compares employee contributions to outsider contributions, and presents the results.

## Implementation

### API

All contributors to the VS Code repo are available for easy access with the Github API, as well as their number of contributions. It is also possible to detect whether a user is a member of Microsoft's GitHub 'organisation' (i.e. whether they are an employee). 

The code in `viz.py` sorts through each contributor, logging their number of contributions and their affiliation with Microsoft. It returns a JSON database with the following style: `{employed:(bool), contribs:(int)}`. (Usernames have been anonymised.)

Note that GitHub's API restricts the number of contributors it returns - currently it only shows the top 365 contributors. This limits our sample to users with at least 3 contributions, but should not change the visualised result too much.

### Visualisation

Various information about the database is visualised on the `index.html` web page using a series of charts, enabled by [Chart.js](https://www.chartjs.org/). You can view the page online [here](https://liam-ol.github.io/csu33012-viz/). (Best viewed on desktop.)

## Requirements

[PyGithub](https://github.com/PyGithub/PyGithub) must be installed to run `viz.py`. You must also replace the `GIT_TOKEN` environment variable with your own access token. (Failing these, you can still use the pre-generated `db.js` file for the visualisation; be warned it will be outdated.)
