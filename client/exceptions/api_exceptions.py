class ApiServerErrorException(Exception):

    def __init__(self, status_code):
        self.status_code = status_code


class UnprocessableEntityException(Exception):

    def __init__(self):
        self.status_code = 422
