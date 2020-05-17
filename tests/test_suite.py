import unittest
from tests.area_tests import AreaTests

test_case_1 = unittest.TestLoader().loadTestsFromTestCase(AreaTests)

# Declare test suite with test cases
test_suite = unittest.TestSuite([test_case_1])

# Execute test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
