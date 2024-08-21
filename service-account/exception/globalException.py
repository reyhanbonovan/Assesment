from fastapi.responses import JSONResponse
from loguru import logger as log

from exception.appException import AppException
from schemas.svcAccountSchemas import ErrorResponse

def global_exception(app):
    @app.exception_handler(Exception)
    async def general_exception_handler(request, exc: Exception):
        log.error(f"Exception type: {type(exc).__name__}")
        log.error(f"Exception message: {str(exc)}")
        response_error = ErrorResponse(code=500, remark="INTERNAL SERVER ERROR")
        # Pastikan ErrorResponse bisa diubah menjadi JSON
        return JSONResponse(status_code=500, content=response_error.dict())
    
    @app.exception_handler(AppException)
    async def custom_exception_handler(request, exc: AppException):
        log.error(f"{exc.code} - {exc.remark}")
        response_error = ErrorResponse(code=exc.code, remark=exc.remark)
        log.info(f"{exc.code} - Failed processing. Response:\n{response_error.dict()}")
        # Pastikan ErrorResponse bisa diubah menjadi JSON
        status_code = exc.code if isinstance(exc.code, int) else 400
        return JSONResponse(status_code=status_code, content=response_error.dict())
