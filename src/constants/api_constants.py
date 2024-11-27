class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_Create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_Create_booking(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)