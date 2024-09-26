from fastapi import Request,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.schemas.general_schemas import ErrorResponseSchema, ErrorDetail
from exceptions.error_codes import ERROR_CODE_MAP
import logging

def get_error_details(status_code: int):
    """
    Helper function to get error details from code_MAP.
    """
    return ERROR_CODE_MAP.get(status_code, ERROR_CODE_MAP["default"])

def http_exception_handler(request, exc: StarletteHTTPException):
    error_info = get_error_details(exc.status_code)

    if exc.status_code == 401:
        # Handle specific case for 401 Unauthorized
        message = "Not authenticated"
        error_details = [ErrorDetail(field=None, detail=message)]
        code = exc.status_code
    elif isinstance(exc.detail, dict):
        message = exc.detail.get("message", error_info["message"])
        errors = exc.detail.get("errors", [])
        code = exc.detail.get("code", error_info["code"])

        error_details = [ErrorDetail(field=error.get("field"), detail=error.get("detail")) for error in errors]
    else:
        message = exc.detail if exc.detail else error_info["message"]
        error_details = [ErrorDetail(field=None, detail=message)]
        code = error_info["code"]

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponseSchema(
            message=message,
            errors=error_details,
            status_code=code,
            status=False
        ).model_dump()
    )


async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        error_detail = {
            "field": error['loc'][1] if len(error['loc']) > 1 else error['loc'][0],
            "message": error['msg']
        }
        errors.append(error_detail)


    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ErrorResponseSchema(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message="Valition failed. please check your input data",
            errors=errors
        ).model_dump()
    )

async def default_exception_handler(request: Request, exc: Exception):
    error_info = get_error_details(500)

    logging.error(str(exc), exc_info=True)

    return JSONResponse(
        status_code=500,
        content=ErrorResponseSchema(
            message=error_info["message"],
            errors=[],
            status_code=500,
            status=False
        ).model_dump()
    )


    