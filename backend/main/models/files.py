import enum

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func

from main.database import Base

class FileExtensinsEnum(enum.Enum):
    VIDEO = 'Видео'
    IMAGE = 'Картинка'
    TXT = 'Текст'
    PDF = 'pdf'
    WORD = 'Word'
    EXCEL = 'Excel'
    ARCHIVE = 'Архив'
    LOGS = 'Логи'
    OTHER = 'Другое'


class FileSourceEnum(enum.Enum):
    MANUAL = 'Админка'
    EMAIL = 'Почта'
    SYSTEM = 'Система'


class FileModel(Base):
    __tablename__ = "files"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    title = Column(
        String(200),
        nullable=False
    )
    description = Column(String)

    original_file_name = Column(
        String(255),
        nullable=False
    )
    file_path = Column(
        String(1024),
        nullable=False
    )
    file_source = Column(
        Enum(FileSourceEnum),
        default=FileSourceEnum.SYSTEM
    )
    extension = Column(
        Enum(FileExtensinsEnum),
        default=FileExtensinsEnum.OTHER
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
