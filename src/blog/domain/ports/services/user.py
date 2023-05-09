from abc import ABC, abstractmethod
from typing import Any, Optional

from blog.domain.model.model import User
from blog.domain.model.schemas import RegisterUserInputDto
from blog.domain.ports.repositories.repository import RepositoryInterface


class UserServiceInterface(ABC):
    @abstractmethod
    def __init__(self, user_repo: RepositoryInterface) -> None:
        raise NotImplementedError

    def create(self, user: RegisterUserInputDto) -> User:
        return self._create(user)

    def get_user_by_user_name(self, user_name: str) -> Optional[tuple[Any, ...]]:
        return self._get_user_by_user_name(user_name)

    def get_user_by_id(self, id_: int) -> Optional[tuple[Any, ...]]:
        return self._get_user_by_id(id_)

    @abstractmethod
    def _create(self, user: RegisterUserInputDto) -> User:
        raise NotImplementedError

    @abstractmethod
    def _get_user_by_user_name(self, user_name: str) -> Optional[tuple[Any, ...]]:
        raise NotImplementedError

    @abstractmethod
    def _get_user_by_id(self, id_: int) -> Optional[tuple[Any, ...]]:
        raise NotImplementedError
