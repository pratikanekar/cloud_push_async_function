from datetime import datetime
import time


def gen_data():
    main_data = []
    panels = 100
    measurements = 10
    device_codes = 20
    zones = 40
    count = 0
    start_time = time.time()

    for panel in range(0, panels):
        # print(f"[PANEL]: {panel}")
        for meas in range(0, measurements):
            mm = f"MEASUREMENT_{meas}"
            # print(f"{mm}")
            for dc in range(0, device_codes):
                device_code = f"DEV_{dc}"
                # print(f"{device_code}")
                for zn in range(0, zones):
                    zone = f"ZON_{zn}"
                    # print(f"{zone}")

                    data_dict = {
                        "measurement": mm,
                        "tags": {
                            "panel_no": panel,
                            "device_code": device_code,
                            "zone": zone,
                            "min_alarm": 0.0,
                            "max_alarm": 0.0,
                            "name": "Down Direction Selected",
                            "alarm_name": "null",
                            "alarm_state": "null",
                            "unique_tag": f"{device_code}-{zone}"
                        },
                        "fields": {
                            "value": 0
                        },
                        "time": datetime.now().replace(microsecond=0).astimezone().isoformat()
                    }
                    count += 1
                    print(data_dict)
                    main_data.append(data_dict)
    print(f"[PROCESS END TIME]: {time.time() - start_time}")
    print(f"{count}")
    return main_data
