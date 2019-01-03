import unittest
import calc_tests


calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcExTests))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)

# testLoad = unittest.TestLoader()
# suites = testLoad.loadTestsFromModule(calc_tests)
#
# testResult = unittest.TestResult()
#
# runner = unittest.TextTestRunner(verbosity=1)
# testResult = runner.run(suites)
# print("errors")
# print(len(testResult.errors))
# print("failures")
# print(len(testResult.failures))
# print("skipped")
# print(len(testResult.skipped))
# print("testsRun")
# print(testResult.testsRun)

# testLoad = unittest.TestLoader()
# suites = testLoad.loadTestsFromModule(calc_tests)
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suites)

# testCases = [calc_tests.CalcBasicTests, calc_tests.CalcExTests]
#
# testLoad = unittest.TestLoader()
#
# suites = []
# for tc in testCases:
#     suites.append(testLoad.loadTestsFromTestCase(tc))
#
# res_suite = unittest.TestSuite(suites)
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(res_suite)

# calcTestSuite = unittest.TestSuite()
# calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcBasicTests))
# calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcExTests))
# print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(calcTestSuite)
