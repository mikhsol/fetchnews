#!/usr/bin/python3
import time
import sys
import logging
from argparse import ArgumentParser

from src.fetcher_runner import TheGuardianFetcherRunner, BbcFetcherRunner
from src.repositories import ArticleMongoDbRepository

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

DESCRIPTION = "News Fetcher - fetch news from news sites based on passed " \
              "parameters and store it in MongoDB database."

sources = {
    "theguardian": TheGuardianFetcherRunner(ArticleMongoDbRepository()),
    "bbc": BbcFetcherRunner(ArticleMongoDbRepository()),
}


class Main(object):
    class Args(object):
        source = "theguardian"
        showList = False

        def __init__(self, s=None, l=False):
            self.source = s
            self.showList = l

    @staticmethod
    def newParser():
        parser = ArgumentParser(prog="fetchnews",
                                usage="python %(prog)s.py -s SOURCE",
                                description=DESCRIPTION)
        parser.add_argument("-s", "--source",
                            help="Source of news. Default value is"
                                 " The Guardian <theguardian>")
        parser.add_argument("-l", action="store_true",
                            help="List of the possible sources.")

        parsed = parser.parse_args()
        return Main.Args(parsed.source, parsed.l)


def final_performance_log(start):
    logger.info("main function processing time: " +
                str(time.process_time() - start))


def main():
    # start = time.process_time()
    status = 0
    arguments = Main().newParser()
    if arguments.showList:
        print(str(sources.keys()).strip("[]"))
        # final_performance_log(start)
        return status

    if not arguments.source:
        arguments.source = "theguardian"

    fr = sources[arguments.source]
    fr.run()

    # final_performance_log(start)
    return status


if __name__ == '__main__':
    sys.exit(main())
