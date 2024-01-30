# main.py

import datetime
import asyncio
from constants import *
from utils import make_api_call, display_api_call_data

async def debug_access_token_info():
    endpoint_params = {
        'input_token': ACCESS_TOKEN,
        'access_token': ACCESS_TOKEN
    }
    url = GRAPH_DOMAIN + '/debug_token'
    return await make_api_call(url, endpoint_params, DEBUG_MODE)

async def get_long_lived_access_token_info():
    endpoint_params = {
        'grant_type': 'fb_exchange_token',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'fb_exchange_token': ACCESS_TOKEN
    }
    url = ENDPOINT_BASE + 'oauth/access_token'
    return await make_api_call(url, endpoint_params, DEBUG_MODE)

async def main():
    response_debug = await debug_access_token_info()
    if response_debug:
        print("\nData Access Expires at:")
        print(datetime.datetime.fromtimestamp(response_debug['json_data']['data']['data_access_expires_at']))

        print("\nToken Expires at:")
        print(datetime.datetime.fromtimestamp(response_debug['json_data']['data']['expires_at']))

    response_long_lived = await get_long_lived_access_token_info()
    if response_long_lived:
        print("\n ---- ACCESS TOKEN INFO ----\n")
        print("Access Token:")
        print(response_long_lived['json_data']['access_token'])

if __name__ == "__main__":
    asyncio.run(main())
