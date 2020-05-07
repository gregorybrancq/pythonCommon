import os
from datetime import datetime, timedelta
from unittest import TestCase

from program import Program


class TestProgram(TestCase):
    def setUp(self):
        self.disable_file = "/tmp/test_program.disable"
        self.modToTest = Program(prog_name="test_program")

    # Check that file is not present
    def test_set_enable(self):
        self.modToTest.progEnable()
        self.assertFalse(os.path.isfile(self.disable_file))

    # Check that file is present
    def test_set_disable(self):
        self.modToTest.progDisable()
        self.assertTrue(os.path.isfile(self.disable_file))

    # Check with a file created more than one day
    def test_is_enable_with_more_than_one_day(self):
        fd = open(self.disable_file, 'w')
        fd.write("2000-01-01 00:00:00.00000")
        fd.close()
        self.assertTrue(self.modToTest.isEnable())
        self.assertFalse(os.path.isfile(self.disable_file))

    # Check with a file created less than one day
    def test_is_enable_with_less_than_one_day(self):
        fd = open(self.disable_file, 'w')
        date_minus_one_hour = datetime.now() - timedelta(hours=1)
        fd.write(str(date_minus_one_hour))
        fd.close()
        self.assertFalse(self.modToTest.isEnable())
        self.assertTrue(os.path.isfile(self.disable_file))
