"""
Error module which contains all error definition related code.
"""
import json
from typing import Dict, Any


class PyBovError(Exception):
    """
    Base project error.
    """

    message: str
    code: int

    def __init__(self, message: str, code: int = 1) -> None:
        """
        Creates a new PyBov error object instance.

        It takes an error messafe and a error code.
        """
        super(PyBovError, self).__init__(message)

        self.message = message
        self.code = code

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the dict representation of the error.
        """
        return {
            'message': self.message,
            'code': self.code
        }

    def as_json(self) -> str:
        """
        Return the json string representation of the error.
        """
        return json.dumps(self.as_dict())
