import time
import requests
import parsel


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
