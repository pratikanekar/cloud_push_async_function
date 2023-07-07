import asyncio
import aiohttp
import time
from json_maker import gen_data


async def send_jsons(jsons):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for json_data in jsons:
            task = asyncio.ensure_future(send_json(session, json_data))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def send_json(session, json_data):
    url = "http://0.0.0.0:5111/test_data/data"
    headers = {'Content-Type': 'application/json'}
    async with session.post(url, json=json_data, headers=headers) as response:
        response_text = await response.text()
        print(f"Response: {response_text}")


main_data = gen_data()
start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(send_jsons(main_data))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time : {execution_time} sec")
