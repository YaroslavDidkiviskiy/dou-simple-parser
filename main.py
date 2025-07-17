import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup

URL_TO_PARSE = "https://jobs.dou.ua/vacancies/?category=Python&exp=0-1"

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, URL_TO_PARSE)
        soup = BeautifulSoup(html, "html.parser")

        vacancies = soup.find_all("li", class_="l-vacancy")

        for vacancy in vacancies:
            title_tag = vacancy.find("a", class_="vt")
            title = title_tag.text.strip()
            link = title_tag["href"]

            location_tag = vacancy.find("span", class_="cities")
            location = location_tag.text.strip() if location_tag else "N/A"

            print(f"{title} | {location} | {link}")



if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(parse())
    end_time = time.time()
    estimated_time = end_time - start_time
    print("-" * 200)
    print(f"Time: {estimated_time}")
