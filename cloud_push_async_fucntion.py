import time
import asyncio
import httpx
from loguru import logger
from json import dumps
from fastapi import HTTPException
from json_maker import gen_data


async def send_data_async(data):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post('http://192.168.1.236:5111/test_data/data', data=data, timeout=250)
            if response.status_code == 200:
                logger.info(f"Response: {response.text}")
                return response
            else:
                logger.critical(f"Response: {response.text}")
    except Exception as e:
        logger.error(f"{e}")


async def main(final_json_data):
    try:
        await send_data_async(final_json_data)
    except Exception as e:
        logger.error(f"{e}")



try:
    logger.info(f"Started Creation of json files.....")
    start_time = time.time()
    main_data = gen_data()
    # final_json_data = dumps(multiple_lists)
    # Run the asynchronous event loop
    logger.info(f"Started Cloud Pushing......")
    for lists in range(0, 1):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(dumps(main_data)))

    logger.debug(f"[Cloud Push Process Time] : {time.time() - start_time}")
except Exception as e:
    logger.error(f"{e}")
