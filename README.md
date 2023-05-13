# Movies Data Project

This project contains scripts for fetching movie data from the Wikidata database, storing the data in an SQLite database, and displaying the data in a table using Flask App Builder.

## Fetch Data

The `fetch_data.py` module queries the Wikidata database for movies released after 2013 that have an IMDb ID. The data is sorted by publication date.

## Store Data

The `store_data` module parses the data fetched by `fetch_data.py` and stores it in an SQLite database. This script has been run once to generate the `movies.db` file, which is included in the zip file.

## Display Data

The `app.py` script uses Flask App Builder to display the data stored in the SQLite database in the form of a table.

## User Credentials

To view the list of movies, you need to log in as an admin user. I created a sample admin user with the following credentials:

- Username: `appsilon`
- Password: `123456`

To create a new admin user, use the `flask fab create-admin` command to reproduce this view on your end.

## Screenshots

The `screenshots` folder contains screenshots of the table view, showing the data sorted by different columns.
