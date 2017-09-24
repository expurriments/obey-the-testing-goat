import os
import subprocess
import sys
import unittest


class DevelopmentEnvironmentTest(unittest.TestCase):
    """Test prerequisites and assumptions about the development environment.

    The outline of what the book is assuming about the software we need
    ready and installed on our computer is available at:
    https://www.obeythetestinggoat.com/book/pre-requisite-installations.html
    
    """

    def check_version(self, program, version_flag='--version'):
        with open(os.devnull, 'w') as f:  # Don't care about the output
            subprocess.run([program, version_flag], check=True, stdout=f)

    def test_running_modern_python3(self):
        self.assertEqual(sys.version_info.major, 3)
        # For the lulz, does not actually matter
        self.assertGreater(sys.version_info.minor, 3)

    def test_django_installed(self):
        try:
            import django
        except ImportError:
            self.fail('Django should be installed and available for use.')

    def test_selenium_installed(self):
        try:
            import selenium
        except ImportError:
            self.fail('Selenium should be installed and available for use.')

    def test_git_installed(self):
        self.check_version('git')

    def test_firefox_installed(self):
        self.check_version('firefox')

    @unittest.skip('I will install it later, now I want it to breeaaak.')
    def test_geckodriver_installed(self):
        self.check_version('geckodriver')




