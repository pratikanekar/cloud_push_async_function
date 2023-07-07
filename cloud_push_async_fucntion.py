import time
import asyncio
import httpx
from loguru import logger
from json import dumps
from json_maker import gen_data


async def send_data_async(data):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post('http://192.168.1.219:5111/test_data/data', data=data)
            if response.status_code == 200:
                logger.info(f"Response: {response.text}")
                return response
    except Exception as e:
        logger.error(f"{e}")


async def main():
    await send_data_async(final_json_data)


try:
    logger.info(f"Started Creation of json files.....")
    start_time = time.time()
    main_data = gen_data()
    final_json_data = dumps(main_data)
    # Run the asynchronous event loop
    logger.info(f"Started Cloud Pushing......")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    logger.debug(f"[Cloud Push Process Time] : {time.time() - start_time}")
except Exception as e:
    logger.error(f"{e}")
