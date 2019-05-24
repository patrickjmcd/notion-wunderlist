# Notion to Wunderlist Integration

A bi-directional syncing tool to copy and update tasks from Notion to Wunderlist.

## Requirements

-   Python3
-   Wunderlist
-   Notion

## Installation

Clone this repository.

## Setup

Create a `.env` file or set environment variables:

-   `NOTION_TOKEN`: the `token_v2` cookie value found by inspecting your browser cookies on a logged-in session on Notion.so
-   `NOTION_TASK_LISTS`: a comma-separated list of Notion URLS for task databases (need fields `Name`, `Assign`, `Status`)
- TODO: KEYS FOR WUNDERLIST DESCRIPTION

## Installation

clone the repository and run:

```Shell
pip3 install .
```

## Running the Script

Run the script by executing:

```Shell
python3 sync.py <Wunderlist-ListName>
```

or

```Shell
python3 -m notion_to_wunderlist.sync <Wunderlist-ListName>
```

## Future Improvements

-   [ ] Turn this into a package with an entry_point for use anywhere.
-   [ ] Enable bi-directional syncing
-   [ ] Better Error-trapping for missing environment variables
