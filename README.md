# location-data toolkit

A collection of example python scripts to manipulate Google Location History data from Google Takeout.

This was designed for personal use only - that is, to manipulate location history data that you own only. Please respect the PII of yourself and others!

## Getting Started

Please use Google Takeout (https://takeout.google.com/settings/takeout) to get a copy of your Location History. You can uncheck all other data and just leave Location History checked. This will be exported to you as a zip of JSON files.

Google Location History is stored as a set of JSON files that contain:
* Activity Segments - A set of activity segments where you have moved from one location to another, with the probability of the mode of transport
* Locations - The set of locations and timestamps where you have been.

This is provided without any support nor additional documentation.

### Prerequisites

You'll need Python 3 on your machine and an active Google account (with Location History activated).  I would also strongly recommend you use virtualenv to install some of the helper packages. Given Location History's JSON isn't well documented, these helper packages will help you reverse engineer the format of the JSON and manipulate them.

You will need one example Google Location history JSON file to generate the classes yourself.

Google Location History will be stored in a set of directories, by year. Each year will contain a set of JSON files by month. warngleDirTree.py will walk this directory tree, convert the data by file and create an output file. This can then be manipulated on standard UNIX tooling to be concatenated, ingested, and processed as you please.

NOTE: I have found that data after July 2019 has a substantially different format / quality.

### Using the Toolkit

Sync this repo and then look at the following scripts:
* [generateClass.sh] - Generates from a Google Location History JSON takeout file JSON Schema and Python Classes to represent the Google Location History data. This is used as there is no documentation of the schema (and code is better than none).
* [usefulScripts.sh] - Some shell scripts to list all the individual Google Location History JSON files, clean up any spurious files you might create (deprecated), and to merge all data for ingestino.
* [wrangle.py] - An example python script to process a single Google Location History JSON file.
* [wrangleDirTree.py] - An example python script that walks a directory tree of Google Location History JSON file inputs, reads them, and outputs for each file the Activity Segments and Locations.
* [queries.sql] - a set of BigQuery SQL 

## Built With

* [genson](https://pypi.org/project/genson/) - a library to reverse engineer JSON Schema from JSON data
* [json-schema-to-class](https://github.com/FebruaryBreeze/json-schema-to-class) - a library to reverse engineer a python class from JSON Schema
* [Pygments] - a useful python library to visualise code in a terminal

## Authors

* **Pak-Ming Wan** - *Initial work*

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](LICENSE.md) file for details