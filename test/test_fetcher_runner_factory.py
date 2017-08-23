import unittest

from src.sources import sources
from src.fetcher_runner import TheGuardianFetcherRunner


class UnknownSourceException(Exception):
    def __init__(self, msg):
        self.msg = msg


class FetcherRunnerFactory(object):
    @staticmethod
    def createRunner(type_):
        if type_ not in sources.keys():
            raise UnknownSourceException("Wrong source of news.")

        if type_ == "theguardian":
            return TheGuardianFetcherRunner()


class TestFetcherRunnerFactory(unittest.TestCase):
    def test_new_factory(self):
        f = FetcherRunnerFactory()
        self.assertTrue(isinstance(f, FetcherRunnerFactory))

    def test_factory_return_exception_on_wrong_source(self):
        self.assertRaises(UnknownSourceException,
                          FetcherRunnerFactory.createRunner, "foo")

    def test_create_the_guardian_fetcher_runner(self):
        self.assertTrue(
            isinstance(FetcherRunnerFactory.createRunner("theguardian"),
                       TheGuardianFetcherRunner))


if __name__ == "__main__":
    unittest.main()
