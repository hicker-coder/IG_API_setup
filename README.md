# IG_API_setup
markdown
Copy code
# Facebook API Python Project

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

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/facebook-api-python-project.git
Install the required dependencies by running:
bash
Copy code
pip install aiohttp
Usage
Configure the constants in the constants.py file with your Facebook API credentials:

ACCESS_TOKEN: Your Facebook access token.
CLIENT_ID: Your Facebook application's client ID.
CLIENT_SECRET: Your Facebook application's client secret.
DEBUG_MODE: Set to 'yes' for debugging, or 'no' for regular output.
PAGE_ID: Your Facebook page ID.
Run the main program using:

bash
Copy code
python main.py
The program will execute the defined asynchronous functions, make API calls, and display the retrieved information.

Project Structure
The project is organized into three main files:

main.py: The main program file that orchestrates the execution of asynchronous functions.

constants.py: Stores constants such as API credentials and debug mode settings.

utils.py: Contains utility functions for making API calls and displaying results.

Constants
Edit the constants.py file to configure your Facebook API credentials and settings. Make sure to replace the placeholder values with your actual credentials.

python
Copy code
GRAPH_DOMAIN = 'https://graph.facebook.com/'
GRAPH_VERSION = 'v18.0'
ENDPOINT_BASE = GRAPH_DOMAIN + GRAPH_VERSION + '/'

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
DEBUG_MODE = 'yes'  # Set to 'yes' for debugging, or 'no' for regular output
PAGE_ID = 'YOUR_PAGE_ID'
Utils
The utils.py file contains utility functions for making asynchronous API calls and displaying the results. It includes make_api_call and display_api_call_data functions.

Main Program
The main.py file is the entry point of the program. It defines asynchronous functions for accessing Facebook API endpoints, such as debug_access_token_info and get_long_lived_access_token_info. The program executes these functions and displays the retrieved information.