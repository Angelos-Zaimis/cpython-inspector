from pydantic import BaseModel, Field

class SourceCodeRequest(BaseModel):
    source: str = Field(
        ...,
        description="Python source code to inspect",
        example="x = 1 + 2"
    )
    python_version: str = Field(
        default="3.12",
        description="Python version to target",
        example="3.12"
    )