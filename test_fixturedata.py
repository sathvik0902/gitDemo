import pytest
import logging

from BaseClass import BaseClass


@pytest.mark.usefixtures("applicationdata")
class TestFixtureData(BaseClass):

        def test_update_profile(self, applicationdata):
            log = self.getLogger()
            log.info(applicationdata[0])
            print(applicationdata[0])
            print(applicationdata[1])