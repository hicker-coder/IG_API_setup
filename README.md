# IG_API_setup

This Python project demonstrates how to interact with the Facebook Graph API using asynchronous code (async/await) and the aiohttp library. It provides examples of retrieving information about access tokens, long-lived access tokens, Instagram accounts, and user pages.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Constants](#constants)
- [Utils](#utils)
- [Main Program](#main-program)
- [Contributing](#contributing)
- [License](#license)


## Getting Started

First, clone the project repository to your local machine:

```shell
git clone https://github.com/yourusername/facebook-api-python-project.git

Configure the constants in the constants.py file with your Facebook API credentials:

ACCESS_TOKEN: Your Facebook access token.
CLIENT_ID: Your Facebook application's client ID.
CLIENT_SECRET: Your Facebook application's client secret.
DEBUG_MODE: Set to 'yes' for debugging, or 'no' for regular output.
PAGE_ID: Your Facebook page ID.



## Main Program
The main.py file is the entry point of the program. It defines asynchronous functions for accessing Facebook API endpoints, such as debug_access_token_info and get_long_lived_access_token_info. The program executes these functions and displays the retrieved information.
