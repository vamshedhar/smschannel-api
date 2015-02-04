from rest_framework.exceptions import APIException


class PermissionError(APIException):
    status_code = 403
    default_detail = 'You do not have permission to perform this action.'


class ValidationError(APIException):
    status_code = 400
    default_detail = 'Data Validation Error'


class UnsupportedError(APIException):
    status_code = 405
    default_detail = 'Method Not Allowed'
