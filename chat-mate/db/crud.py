from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel
from db.models import User, Message, Status, Group
from db.dtos import UserRegistrationDto, UserProfileDto, MessageDto, StatusDto, GroupDto, GroupMemberDto
from datetime import datetime

# Database setup
global engine
engine = create_engine('sqlite:///chat-mate/db/chatmate.db')
global Session
Session = sessionmaker(bind=engine)
global session
session = Session()

# User CRUD
def add_user(user_dto: UserRegistrationDto):
    user = User(
        first_name=user_dto.first_name,
        last_name=user_dto.last_name,
        user_name=user_dto.user_name,
        phone_number=user_dto.phone_number,
        password=user_dto.password,
        profile_picture_url = "https://th.bing.com/th/id/OIP.4Q7-yMnrlnqwR4ORH7c06AHaHa?rs=1&pid=ImgDetMain"
    )
    session.add(user)
    session.commit()
    return user

def get_user(user_id: int):
    return session.query(User).filter(User.user_id == user_id).first()

def update_user(user_id: int, user_dto: UserProfileDto):
    user = get_user(user_id)
    if user:
        user.first_name = user_dto.first_name
        user.last_name = user_dto.last_name
        user.user_name = user_dto.user_name
        user.profile_picture_url = user_dto.profile_picture_url,
        #user.password = user_dto.
        session.commit()
    return user

def delete_user(user_id: int):
    user = get_user(user_id)
    if user:
        session.delete(user)
        session.commit()
    return user

# Message CRUD
def add_message(message_dto: MessageDto):
    message = Message(
        content=message_dto.content,
        timestamp=message_dto.timestamp,
        sender_id=message_dto.sender_id,
        receiver_id=message_dto.receiver_id,
        group_id=message_dto.group_id
    )
    session.add(message)
    session.commit()
    return message

def get_message(message_id: int):
    return session.query(Message).filter(Message.message_id == message_id).first()

def update_message(message_id: int, message_dto: MessageDto):
    message = get_message(message_id)
    if message:
        message.content = message_dto.content
        message.timestamp = message_dto.timestamp
        message.sender_id = message_dto.sender_id
        message.receiver_id = message_dto.receiver_id
        message.group_id = message_dto.group_id
        session.commit()
    return message

def delete_message(message_id: int):
    message = get_message(message_id)
    if message:
        session.delete(message)
        session.commit()
    return message

# Status CRUD
def add_status(status_dto: StatusDto):
    status = Status(
        content=status_dto.content,
        timestamp=status_dto.timestamp,
        media_url=status_dto.media_url,
        user_id=status_dto.user_id
    )
    session.add(status)
    session.commit()
    return status

def get_status(status_id: int):
    return session.query(Status).filter(Status.status_id == status_id).first()

def update_status(status_id: int, status_dto: StatusDto):
    status = get_status(status_id)
    if status:
        status.content = status_dto.content
        status.timestamp = status_dto.timestamp
        status.media_url = status_dto.media_url
        status.user_id = status_dto.user_id
        session.commit()
    return status

def delete_status(status_id: int):
    status = get_status(status_id)
    if status:
        session.delete(status)
        session.commit()
    return status

# Group CRUD
def add_group(group_dto: GroupDto):
    group = Group(
        name=group_dto.name,
        description=group_dto.description,
        group_picture_url=group_dto.group_picture_url
    )
    session.add(group)
    session.commit()
    return group

def get_group(group_id: int):
    return session.query(Group).filter(Group.group_id == group_id).first()

def update_group(group_id: int, group_dto: GroupDto):
    group = get_group(group_id)
    if group:
        group.name = group_dto.name
        group.description = group_dto.description
        group.group_picture_url = group_dto.group_picture_url
        session.commit()
    return group

def delete_group(group_id: int):
    group = get_group(group_id)
    if group:
        session.delete(group)
        session.commit()
    return group

def add_group_member(group_id: int, user_id: int):
    group = get_group(group_id)
    user = get_user(user_id)
    if group and user:
        group.members.append(user)
        session.commit()
    return group

def remove_group_member(group_id: int, user_id: int):
    group = get_group(group_id)
    user = get_user(user_id)
    if group and user:
        group.members.remove(user)
        session.commit()
    return group
