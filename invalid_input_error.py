from base_error import BaseError


class InvalidInputError(BaseError):
    def __init__(self, message):
        super()
