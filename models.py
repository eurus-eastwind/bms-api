from sqlalchemy.sql.expression import null
from config import Base
from sqlalchemy import String, Boolean, Integer, Column, text, Date, DateTime
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'admin'

    admin_id = Column(String(36), primary_key=True,
                nullable=False, default=text('UUID()'))
    admin_fname = Column(String(255), nullable=False)
    admin_mname = Column(String(255), nullable=True)
    admin_lname = Column(String(255), nullable=False)
    admin_suffix = Column(String(255), nullable=True)
    admin_profile_pic = Column(String(255), nullable=False)
    admin_contact = Column(String(255), nullable=False)
    admin_email = Column(Date, nullable=False)
    admin_password = Column(String(255), nullable=False)
    admin_status = Column(String(255), nullable=False)
    admin_role = Column(String(255), nullable=False)
    admin_created_by = Column(String(255), nullable=False)
    admin_updated_by = Column(String(255), nullable=False)
    admin_created_at  = Column(DateTime, default=text('NOW()'))
    admin_updated_at  = Column(DateTime, default=text('NOW()'))

