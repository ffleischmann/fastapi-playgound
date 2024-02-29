from models import ArticleModel, BasicResponseModel, AllArticlesResponseModel
from fastapi import HTTPException
from article import Article
from fastapi import APIRouter

router = APIRouter()

@router.get("/articles/{article_id}")
def get_article_by_id(article_id: int) -> ArticleModel:
    article = Article()
    response = article.get_article_by_id(article_id)
    if response == False:
        raise HTTPException(status_code=404, detail=f"article does not exist")
    return response

@router.post("/articles/", status_code=201)
def safe_new_article(payload: ArticleModel) -> BasicResponseModel:
    article = Article()
    new_article_id = article.safe_new_article(payload)
    return {"message": f"article {new_article_id} created"}


@router.get("/articles/")
def get_articles():
    article = Article()
    articles = article.get_all_articles()
    return articles