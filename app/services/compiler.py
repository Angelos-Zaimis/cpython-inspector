import sys
from app.core.exceptions import InvalidSourceCode 

def compile_source_code(source_code: str) -> object:
    try:
        return compile(source_code, "<string>", "exec")
    except SyntaxError as e:
        raise InvalidSourceCode(detail=f"SyntaxError on line {e.lineno}: {e.msg}")

def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}"
