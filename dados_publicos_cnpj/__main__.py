import aiohttp


async def check_url_availability(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return 200 <= response.status < 300

        except aiohttp.ClientError:
            return False
