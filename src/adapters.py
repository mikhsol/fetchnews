def article_dict_adapter(article):
    return {"authors": article.authors,
            "headline": article.headline,
            "text": article.text,
            "url": article.url,
            "date": article.date,
            "id": article.id}
