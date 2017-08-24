import logging
import sys
from aiohttp import web
import asyncio

from src.repositories import ArticleMongoDbRepository

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


async def get_articles():
    r = ArticleMongoDbRepository()
    r.connect()
    a = r.get_all()
    r.close()
    return a


async def articles(request):
    a = await get_articles()
    return web.json_response(a)


async def search_by_keywords(k):
    r = ArticleMongoDbRepository()
    r.connect()
    a = r.search_by_keywords(k)
    r.close()
    return a


async def search(request):
    k = request.match_info["keywords"].split(",")
    a = await search_by_keywords(k)
    return web.json_response(a)


async def build_server(loop):
    app = web.Application()
    app.router.add_get("/articles", articles)
    app.router.add_get("/articles/{keywords}", search)
    return await loop.create_server(app.make_handler(), "localhost", 8080)


def main():
    loop = asyncio.get_event_loop()

    loop.run_until_complete(build_server(loop))
    logger.info("Server ready!")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Shutting Down!")
        loop.close()
        return 0


if __name__ == "__main__":
    sys.exit(main())
