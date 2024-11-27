import allure
import pytest

class TestCreateBokking(object):

    @pytest.mark.posiitive
    @allure.title("Verify that create booking status and booking ID should not be null")
    @allure.description("Create a booking from paayload and verify that booking id shouldd not be null")
    def test_Create_booking(self):
        pass