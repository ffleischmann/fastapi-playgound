from pydantic import BaseModel, Field

class ArticleModel(BaseModel):
    ean: int
    name: str = Field(min_length=1, description="name can not be empty")
    size: int
    brand: str = Field(min_length=1, description="brand name can not be empty")

class BasicResponseModel(BaseModel):
    message: str

class NameResponse(BaseModel):
    message: list

# @TODO: how to make a model that defines a variable key name / type as key name
class AllArticlesResponseModel(BaseModel):
    articleid: ArticleModel