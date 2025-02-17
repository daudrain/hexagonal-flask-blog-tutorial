import datetime
from uuid import uuid4

from pydantic import BaseModel, field_validator, FieldValidationInfo, UUID4
from pydantic.fields import Field
from werkzeug.security import generate_password_hash


class RegisterUserInputDto(BaseModel):
    uuid: str
    user_name: str
    password: str


class RegisterUserOutputDto(BaseModel):
    uuid: str
    user_name: str


def register_user_factory(user_name: str, password: str) -> RegisterUserInputDto:
    # You can initialize uuid in factory or see below for pydantic usage
    return RegisterUserInputDto(
        uuid=str(uuid4()),
        user_name=user_name,
        password=generate_password_hash(password),
    )


class CreatePostInputDto(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    author_id: UUID4
    title: str
    body: str
    created: datetime.datetime = Field(default_factory=datetime.datetime.now)

    # Possible place for custom validators, or it can be delegated to factory

    @field_validator("body")
    @classmethod
    def body_length(cls, v: str):
        if len(v) > 10000:
            raise ValueError("Body length must be maximum of 10000 characters")
        return v

    @field_validator("title")
    @classmethod
    def title_length(cls, v: str):
        if len(v) > 100:
            raise ValueError("Title length must be maximum of 100 characters")
        return v

    @field_validator("title", "body")
    @classmethod
    def title_and_body_should_not_be_empty(
        cls, v: str, info: FieldValidationInfo
    ) -> str:
        if not v:
            raise ValueError("Title and body must not be empty or None")
        return v


def create_post_factory(title: str, body: str, author_id: UUID4) -> CreatePostInputDto:
    return CreatePostInputDto(title=title, body=body, author_id=author_id)


class UpdatePostInputDto(BaseModel):
    uuid: str
    title: str
    body: str


def update_post_factory(uuid: str, title: str, body: str) -> UpdatePostInputDto:
    return UpdatePostInputDto(uuid=uuid, title=title, body=body)


class DeletePostInputDto(BaseModel):
    uuid: str


def delete_post_factory(uuid: str) -> DeletePostInputDto:
    return DeletePostInputDto(uuid=uuid)
