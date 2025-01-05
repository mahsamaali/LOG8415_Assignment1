
import asyncio
import aiohttp
import time

async def call_endpoint_http(session, request_num):
    url = "http://my-load-balancer-1940589805.us-east-1.elb.amazonaws.com:8000"  # Load balancer URL here
    headers = {'content-type': 'application/json'}
    try:
        async with session.get(url, headers=headers) as response:
            status_code = response.status
            # Check content type before parsing as JSON
            if response.headers.get('content-type') == 'application/json':
                response_data = await response.json()
            else:
                response_data = await response.text()
            
            print(f"Request {request_num}: Status Code: {status_code}, Response: {response_data}")
            return status_code, response_data
    except Exception as e:
        print(f"Request {request_num}: Failed - {str(e)}")
        return None, str(e)

async def main():
    num_requests = 1000
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [call_endpoint_http(session, i) for i in range(num_requests)]
        await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / num_requests
    print(f"\nTotal time taken: {total_time:.2f} seconds")
    print(f"Average time per request: {average_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
