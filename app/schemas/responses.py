from typing import Optional, Any

from pydantic import BaseModel, Field

class InstructionResponse(BaseModel):
    offset: int = Field(
        ..., 
        description="Bytecode offset of the instruction",
        example=0
    )
    
    opname: str = Field(
        ...,
        description="Human-readable name of the opcode",
        example="LOAD_CONST" 
    )
    
    arg: Optional[int] = Field(
        None,
        description="Numeric argument for the instruction, if applicable",
        example=1
    )
    
    argval: Optional[Any] = Field(
        None,
        description="Resolved value of the argument, if applicable",
        example="x"
    )
    
    description: str = Field(
        ...,   
        description="Human-readable description of the instruction's effect",
        example="Pushes the constant 1 onto the stack"
    )

class BytecodeResponse(BaseModel):
    source: str = Field(
        ...,
        description="Original Python source code",
        example="x = 1 + 2"
    )
    
    python_version: str = Field(
        ...,
        description="Python version targeted for bytecode generation",
        example="3.12"
    )
    
    instructions: list[InstructionResponse] = Field(
        ...,
        description="List of bytecode instructions generated from the source code"
    )  
    