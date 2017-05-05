import os
import sys
import unittest
from sys import argv
from time import gmtime, strftime


class AutomateTesting:
    """
    Used to run all selenium unittest tests.
    """
    # CONSTANTS:
    testLogDir = '/testLogs/'

    def __init__(self, logName=''):
        self.set_log_file_path(logName)
        self.testLoader = unittest.TestLoader()
        self.testSuite = self.testLoader.discover(os.path.dirname(
                                                                                          os.path.dirname(
                                                                                              os.path.dirname(
                                                                                                  os.path.abspath(__file__)))),
                                                  pattern='test_*.py')

    def run_tests(self):
        """
        Runs the loaded test suite stored in self.testSuite.  Outputs the
        results to the log file specified by self.logFilePath.
        """
        with open(self.logFilePath, 'w') as logStream:
            textRunner = unittest.TextTestRunner(stream=logStream, verbosity=2)
            textRunner.run(self.testSuite)

    def set_log_file_path(self, logName):
        """
        Set the self.logFilePath based on logName.  First checks to see
        that the log directory exists; if not, makes it.
        """
        logFileName = strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + \
            logName + '.txt'
        logDirPath = os.path.dirname(os.path.abspath(__file__)) + \
            self.testLogDir
        if not os.path.isdir(logDirPath):
            os.mkdir(logDirPath)
        else:
            pass
        self.logFilePath = logDirPath + logFileName
        print("PATH TO LOG FILE:\n{}".format(self.logFilePath))


if __name__ == '__main__':
    if len(argv) > 2:
        autoTest = AutomateTesting(logName=argv[1])
    else:
        autoTest = AutomateTesting()
    autoTest.run_tests()
