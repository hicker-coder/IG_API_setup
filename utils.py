# utils.py

import aiohttp
import json

async def make_api_call(url, endpoint_params, debug='no'):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=endpoint_params) as response:
            data = await response.json()
            response = {
                'url': url,
                'endpoint_params': endpoint_params,
                'endpoint_params_pretty': json.dumps(endpoint_params, indent=4),
                'json_data': data,
                'json_data_pretty': json.dumps(data, indent=4)
            }
            if debug == 'yes':
                display_api_call_data(response)
            return response

def display_api_call_data(response):
    print("\nURL:")
    print(response['url'])
    print("\nEndpoint Params:")
    print(response['endpoint_params_pretty'])
    print("\nResponse:")
    print(response['json_data_pretty'])
