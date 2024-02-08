from pydantic import BaseModel


class GetArticleModel(BaseModel):
    id: str
    title: str
    content: str


class GetArticlesModel(BaseModel):
    items: list[GetArticleModel]


class CreateArticleModel(BaseModel):
    title: str
    content: str


class LoginModel(BaseModel):
    username: str
    password: str


class ErrorModel(BaseModel):
    detail: str