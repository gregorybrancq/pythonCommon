import os
from unittest import TestCase
from datetime import datetime, timedelta

from progDisEn import ProgEnDis


class TestProgEnDis(TestCase):
    def setUp(self):
        self.disableFile = "/tmp/test_progDisEn"
        self.modToTest = ProgEnDis(disableFile=self.disableFile)

    # Check that file is not present
    def test_set_enable(self):
        self.modToTest.setEnable()
        self.assertFalse(os.path.isfile(self.disableFile))

    # Check that file is present
    def test_set_disable(self):
        self.modToTest.setDisable()
        self.assertTrue(os.path.isfile(self.disableFile))

    # Check with a file created more than one day
    def test_is_enable_with_more_than_one_day(self):
        fd = open(self.disableFile, 'w')
        fd.write("2000-01-01 00:00:00.00000")
        fd.close()
        self.assertTrue(self.modToTest.isEnable())

    # Check with a file created less than one day
    def test_is_enable_with_less_than_one_day(self):
        fd = open(self.disableFile, 'w')
        dateMinusOneHour = datetime.now() - timedelta(hours=1)
        fd.write(str(dateMinusOneHour))
        fd.close()
        self.assertFalse(self.modToTest.isEnable())
