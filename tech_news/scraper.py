import time
import requests
import parsel

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(text=html_content)

    news = selector.css(".cs-overlay-link::attr(href)").getall()

    if not news:
        return []

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)

    next_page = selector.css(".next::attr(href)").get()

    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(text=html_content)

    news_info = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "reading_time": int(
            selector.css(".meta-reading-time::text").re_first(r"(\d+)")
        ),
        "summary": selector.xpath(
            "string(//div[contains(@class, 'content')]//p[1])").get().strip(),
        "category": selector.css(".meta-category .label::text").get(),
    }

    return news_info


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com/"

    news = []

    while len(news) < amount:
        html_content = fetch(URL_BASE)
        news_links = scrape_updates(html_content)

        for link in news_links:
            if len(news) == amount:
                break

            news_html = fetch(link)
            news_info = scrape_news(news_html)
            news.append(news_info)

        next_page_link = scrape_next_page_link(html_content)
        if not next_page_link:
            break

        URL_BASE = next_page_link

    create_news(news)

    return news
