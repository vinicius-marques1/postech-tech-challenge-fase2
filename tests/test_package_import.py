import unittest

import route_optimizer


class PackageImportTest(unittest.TestCase):
    def test_package_can_be_imported(self):
        self.assertIsNotNone(route_optimizer.__doc__)


if __name__ == "__main__":
    unittest.main()
