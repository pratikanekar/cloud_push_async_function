from datetime import datetime
import time
from loguru import logger


def gen_data():
    try:
        main_data = []
        panels = 100
        measurements = 10
        device_codes = 20
        zones = 60

        for panel in range(0, panels):
            count = 0
            start_time = time.time()
            pan = f"PANEL_{panel}"
            for meas in range(0, measurements):
                mm = f"MEASUREMENT_{meas}"
                for dc in range(0, device_codes):
                    device_code = f"DEV_{dc}"
                    for zn in range(0, zones):
                        zone = f"ZON_{zn}"
                        data_dict = [{
                            "measurement": mm,
                            "tags": {
                                "panel_no": pan,
                                "device_code": device_code,
                                "zone": zone,
                                "min_alarm": 0.0,
                                "max_alarm": 0.0,
                                "name": "Down Direction Selected",
                                "alarm_name": "null",
                                "uuid_tag": f"{panel}_{device_code}_{zone}",
                                "alarm_state": "null",
                                "unique_tag": f"{device_code}-{zone}"
                            },
                            "fields": {
                                "value": 0
                            },
                            "time": datetime.now().replace(microsecond=0).astimezone().isoformat()
                        }]
                        count += 1
                        main_data.append(data_dict)
            logger.debug(f"[JSON Making Process Time]: {time.time() - start_time}")
            logger.debug(f"{count}")
        # print(main_data)
        return main_data
    except Exception as e:
        logger.info(f"{e}")
# gen_data()
