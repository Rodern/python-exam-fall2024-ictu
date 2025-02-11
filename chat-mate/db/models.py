from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association table for many-to-many relationship between Users and Groups
group_members = Table('group_members', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.group_id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)  # Ensure password field is included
    profile_picture_url = Column(String)

    messages_sent = relationship('Message', foreign_keys='Message.sender_id', back_populates='sender')
    messages_received = relationship('Message', foreign_keys='Message.receiver_id', back_populates='receiver')
    status_updates = relationship('Status', back_populates='user')
    groups = relationship('Group', secondary=group_members, back_populates='members')

class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    receiver_id = Column(Integer, ForeignKey('users.user_id'))
    group_id = Column(Integer, ForeignKey('groups.group_id'), nullable=True)

    sender = relationship('User', foreign_keys=[sender_id], back_populates='messages_sent')
    receiver = relationship('User', foreign_keys=[receiver_id], back_populates='messages_received')
    group = relationship('Group', back_populates='messages')

class Status(Base):
    __tablename__ = 'status_updates'
    status_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    media_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship('User', back_populates='status_updates')

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    group_picture_url = Column(String)

    members = relationship('User', secondary=group_members, back_populates='groups')
    messages = relationship('Message', back_populates='group')


from sqlalchemy import create_engine

# Replace 'chatmate.db' with your desired database name
engine = create_engine('sqlite:///chat-mate/db/chatmate.db')

# Create all tables
Base.metadata.create_all(engine)
