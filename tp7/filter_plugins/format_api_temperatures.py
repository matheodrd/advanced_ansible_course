def format_api_temperatures(api_hourly: dict) -> list[dict]:
    """
    Transform open meteo API hourly temperature data into a list of dicts
    [{'time': ..., 'temperature': ...}].
    """
    times = api_hourly.get("time", [])
    temps = api_hourly.get("temperature_2m", [])
    count = min(len(times), len(temps))
    return [
        {"time": times[i], "temperature": str(temps[i])}
        for i in range(count)
    ]

class FilterModule():
    def filters(self) -> dict:
        return {
            "format_api_temperatures": format_api_temperatures
        }
