from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional

from main.models import FileSourceEnum, FileExtensinsEnum

class FileBase(BaseModel):
    title: str
    description: Optional[str] = None
    original_file_name: str
    file_source: FileSourceEnum = FileSourceEnum.SYSTEM
    extension: FileExtensinsEnum = FileExtensinsEnum.OTHER


class FileCreate(FileBase):
    file_path: str


class FileUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    file_path: Optional[str] = None


class FileRead(FileBase):
    id: int
    file_path: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
