from datetime import datetime
from tech_news.database import db


# Requisito 7
def search_by_title(title):
    title = title.lower()

    news = db.news.find({"title": {"$regex": title, "$options": "i"}})

    result = [(new["title"], new["url"]) for new in news]

    return result


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(
            date, "%Y-%m-%d").strftime("%d/%m/%Y")

    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": formatted_date})

    result = [(new["title"], new["url"]) for new in news]

    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
