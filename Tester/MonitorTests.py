import unittest
from Main import loadreleases
import asyncio
class TestAsyncMethods(unittest.TestCase):

    def testInitialLinks(results):
        "Test links are being retrieved properly"
        asyncio.run(loadreleases)
        results = str()
