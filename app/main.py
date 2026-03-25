from fastapi import FastAPI
from app.core.config import settings
from app.core.exceptions import (
    InvalidSourceCode,
    UnsupportedPythonVersion,
    invalid_source_code_handler,
    unsupported_version_handler,
)

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

app.add_exception_handler(InvalidSourceCode, invalid_source_code_handler)
app.add_exception_handler(UnsupportedPythonVersion, unsupported_version_handler)

app.get("/")
def root():
    return {
        "project": "CPython Inspector",
        "version": "0.1.0",
        "description": "Inspect CPython internals — bytecode, stack simulation, AST pipeline.",
        "docs": "/docs",
    }