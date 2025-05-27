# Schema for AI

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AiSchema(BaseModel):

    execution: Optional[datetime] = Field(description='API execution time')
    file_name: str = Field(description='Name of file')
    extension_file_name: str = Field(description='Extension name of file')
    url_ia: str = Field(description='Address of Ai (url used)')
    prompt_ia: Optional[str] = Field(description='PROMPT used in AI')
    status: str = Field(description='Execution status example - OK, ERROR')
    status_api: str = Field(description='Status execution in api example - 200, 404, 500')
    error_api: Optional[str] = Field(description='In case of an error in the API this field will be filled in')
    ai_error: Optional[str] = Field(description='In case of an error in the AI this field will be filled in')
    ai_text_success: Optional[str] = Field(description='Every time the AI is successful in responding it will fill this field')

    class Config:
        from_attributes = True
