# Mini Project 1 - API Client

## Author

Adeola Ajayi  
INF601 - Advanced Programming in Python

## Description

This project is an object-oriented Python client for the Practice Hub REST API.

The program authenticates using an API token and demonstrates these operations:

- Create a post.
- List posts, including filtering for my own posts.
- Read a single post by ID.
- Update one of my posts.
- Delete one of my posts.

The client includes handling for HTTP errors 401, 403, 404, and 422.

## Requirements

- Python 3.13
- requests
- A Practice Hub account and valid API token
- An internet connection

## Installation

Open a terminal in the project folder and install the required package:

```bash
python3 -m pip install -r requirements.txt
```

## API Token

Store the Practice Hub API token in an environment variable.

Do not place your real token in the Python code, this README, or GitHub.

On macOS or Linux, run:

```bash
export PRACTICE_API_TOKEN="your-token-here"
```

Replace the placeholder with your actual token only when entering the command
in your terminal.

Set the environment variable again when opening a new terminal.

## Running the Program

In the same terminal where the token is set, run:

```bash
python3 client.py
```

The program creates a test post, retrieves it, updates it, lists my posts,
and deletes the test post it created. It prints progress messages and
returned data.

## Error Handling

The client prints readable messages for these HTTP errors:

- 401: Missing or incorrect API token.
- 403: Attempting to modify another user's post.
- 404: The requested post does not exist.
- 422: Invalid request data. The API's validation details are displayed.

## AI Usage

I used ChatGPT to explain the assignment requirements, generate portions of the Python code and README documentation, and help troubleshoot errors. I also used Claude Code to assist with parts of the program and troubleshooting.

I entered and adapted the code, reviewed it, and tested it against the Practice Hub API. I checked the create, read, update, list, and delete operations and tested the handling of HTTP errors 401, 403, 404, and 422.

