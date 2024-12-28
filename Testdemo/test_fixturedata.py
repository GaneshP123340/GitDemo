# import pytest
#
#
# @pytest.mark.usefixtures("dataload")
# class TestExample2:
#
#     def test_editProfile(self, dataload):
#         print(dataload)


import pytest

from Testdemo.BaseClass import BaseClass


#
# from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editProfile(self, dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[2])
        # print(dataload)






