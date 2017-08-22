#!/usr/bin/python3
import time
import sys
import logging
from argparse import ArgumentParser

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

DESCRIPTION = "News Fetcher - fetch news from news sites based on passed " \
              "parameters and store it in MongoDB database."

# default news source
THE_GUARDIAN = "theguardian"
# ths BBC source
BBC = "bbc"
SOURCES = [THE_GUARDIAN, BBC]


class Main(object):
    class Args(object):
        source = THE_GUARDIAN
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
                                 " The Guardian <" + THE_GUARDIAN + ">")
        parser.add_argument("-l", action="store_true",
                            help="List of the possible sources.")

        parsed = parser.parse_args()
        return Main.Args(parsed.source, parsed.l)


def final_performance_log(start):
    logger.info("main function processing time: " +
                str(time.process_time() - start))


def main():
    start = time.process_time()

    status = 0
    arguments = Main().newParser()
    if arguments.showList:
        print(str(SOURCES).strip("[]"))
        final_performance_log(start)
        return status

    if not arguments.source:
        arguments.source = THE_GUARDIAN

    print(arguments.source)

    final_performance_log(start)
    return status


if __name__ == '__main__':
    sys.exit(main())
