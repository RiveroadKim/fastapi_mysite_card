# ORM: 테이블 -> 객체화

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MessageORM(Base):
  __tablename__ = "tbl_message" # 실제 테이블 명

  no = Column(Integer, primary_key=True, index=True)
  name = Column(String) # String 길이 제한 있음
  email = Column(String, nullable=False) # String 길이 제한 있음
  message = Column(Text, nullable=False) # Text 길이 제한 없음
  create_date = Column(DateTime, nullable=False)

  def __init__(self, name, email, message, create_date):
    self.name = name
    self.email = email
    self.message = message
    self.create_date = create_date
    