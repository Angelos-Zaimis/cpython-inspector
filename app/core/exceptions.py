from fastapi import Request
from fastapi.responses import JSONResponse

class InvalidSourceCode(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        
class UnsupportedPythonVersion(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        
def invalid_source_code_handler(request: Request, exc: InvalidSourceCode):
    return JSONResponse(
        status_code=400,
        content={
            "error": "InvalidSourceCode",
            "detail": exc.detail,
        }
    )
    
def unsupported_version_handler(request: Request, exc: UnsupportedPythonVersion):
    return JSONResponse(
        status_code=400,
        content={
            "error": "UnsupportedPythonVersion",
            "detail": exc.detail,
        }
    )