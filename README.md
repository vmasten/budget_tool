# Project Name
Budget Tool

**Author**: Vince Masten
**Version**: 1.0.1

## Overview
An HTTP server built in Django that allows for the creation of a user account and the storing of budgets and transactions in a database. Currently in development.

## Getting Started
1. Download the repo
1. Ensure your virtual environment matches that of the Pipfile
1. Install Docker Desktop if needed, then spin up the container with docker-compose up
1. Create a super user. Go to localhost:8000 to create a new regular user, and then watch your docker-compose terminal window for the activation link. Once that's done, you can manually add budgets and transactions in Django Admin and see them displayed per user.

## Architecture
Uses Python, pipenv (with a variety of packages--see Pipfile for more information) and Django as a framework for loading and rendering the pages.

## Change Log

Author: Vince Masten <vmasten@me.com>
Date:   Tue Jan 22 14:59:06 2019 -0800

    refactor

Author: Vince Masten <vmasten@me.com>
Date:   Mon Jan 21 22:24:49 2019 -0800

    added README

Author: Vince Masten <vmasten@me.com>
Date:   Mon Jan 21 22:20:27 2019 -0800

    time for bed

Author: Vince Masten <vmasten@me.com>
Date:   Mon Jan 21 13:23:51 2019 -0800

    Initial commit
