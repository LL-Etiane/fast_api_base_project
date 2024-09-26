ERROR_CODE_MAP = {
    400: {
        "code": 400,
        "message": "The request is invalid.",
        "description": "The server could not understand the request due to invalid syntax."
    },
    401: {
        "code": 401,
        "message": "Authentication credentials were not provided or are invalid.",
        "description": "The request requires user authentication."
    },
    403: {
        "code": 403,
        "message": "You do not have permission to access this resource.",
        "description": "The server understands the request, but the client does not have the necessary permissions."
    },
    404: {
        "code": 404,
        "message": "The requested resource could not be found.",
        "description": "The server can't find the requested resource."
    },
    405: {
        "code": 405,
        "message": "The request method is not allowed for this resource.",
        "description": "The method specified in the request is not allowed for the resource."
    },
    409: {
        "code": 409,
        "message": "A conflict occurred with the current state of the resource.",
        "description": "The request could not be processed because of conflict in the current state of the resource."
    },
    422: {
        "code": 422,
        "message": "Validation error occurred.",
        "description": "The server understands the content type of the request, but the request body is syntactically incorrect or fails validation."
    },
    429: {
        "code": 429,
        "message": "Too many requests have been made in a short time. Please try again later.",
        "description": "The user has sent too many requests in a given amount of time ('rate limiting')."
    },
    500: {
        "code": 500,
        "message": "An internal server error occurred.",
        "description": "The server encountered an unexpected condition that prevented it from fulfilling the request."
    },
    502: {
        "code": 502,
        "message": "The server received an invalid response from an upstream server.",
        "description": "The server was acting as a gateway or proxy and received an invalid response from the upstream server."
    },
    503: {
        "code": 503,
        "message": "The server is currently unavailable. Please try again later.",
        "description": "The server is currently unable to handle the request due to temporary overloading or maintenance."
    },
    504: {
        "code": 504,
        "message": "The server took too long to respond.",
        "description": "The server was acting as a gateway or proxy and did not receive a timely response from the upstream server."
    },
    "default": {
        "code": 500,
        "message": "An error occurred.",
        "description": "There was a server error"
    }
}