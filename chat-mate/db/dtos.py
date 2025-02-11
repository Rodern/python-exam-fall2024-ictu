from pydantic import BaseModel
from datetime import datetime

# User DTOs
class UserRegistrationDto(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    user_name: str
    phone_number: str
    password: str  # Add password field

class UserLoginDto(BaseModel):
    user_name: str
    phone_number: str
    password: str

class UserProfileDto(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    profile_picture_url: str

# Message DTO
class MessageDto(BaseModel):
    content: str
    timestamp: datetime
    sender_id: int
    receiver_id: int
    group_id: int = None

# Status DTO
class StatusDto(BaseModel):
    content: str
    timestamp: datetime
    media_url: str
    user_id: int

# Group DTO
class GroupDto(BaseModel):
    name: str
    description: str
    group_picture_url: str

class GroupMemberDto(BaseModel):
    user_id: int
