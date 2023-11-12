import aiohttp
import asyncio

async def fetch_weather_data(api_key, location, date):
    url = f'http://api.weatherapi.com/v1/future.json?key={api_key}&q={location}&dt={date}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

class WeatherChecker:
    def __init__(self, api_key):
        self.api_key = api_key  

    async def check_rain(self, location, date):
        try:
            data = await fetch_weather_data(self.api_key, location, date)

            if "forecast" in data and "forecastday" in data["forecast"] and data["forecast"]["forecastday"]:
                for hour_section in data["forecast"]["forecastday"][0]["hour"]:
                    if hour_section["will_it_rain"] == 1:
                        return True  # It will rain
                else:
                    return False  # It will NOT rain
            else:
                raise ValueError("Invalid data format in the API response.")
        except Exception as e:
            raise RuntimeError(f"Error: {e}")

# Example usage:
async def main():
    api_key = 'ea2af1037f4540a4844235921231111'
    location = 'Amritsar'
    date = '2023-12-13'

    weather_checker = WeatherChecker(api_key)
    is_raining = await weather_checker.check_rain(location, date)

    if is_raining:
        print("It will rain today")
    else:
        print("It will NOT rain today")

if __name__ == "__main__":
    asyncio.run(main())
