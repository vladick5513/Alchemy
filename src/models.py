from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_256
import enum
import datetime
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
creared_on = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_on = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str]

    resumes: Mapped[list["ResumesOrm"]] = relationship("ResumesOrm", back_populates="worker")

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_on: Mapped[creared_on]
    updated_on: Mapped[updated_on]

    worker: Mapped["WorkersOrm"] = relationship("WorkersOrm", back_populates="resumes")

    repr_cols_num = 4
    repr_cols = ("updated_on", )



































metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer,primary_key=True),
    Column("username", String),
)