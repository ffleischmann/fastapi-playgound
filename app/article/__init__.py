from models import ArticleModel

# Replaces a DB
ARTICLES = {
    0: ArticleModel(ean=1234, name="T-Shirt", size=35, brand="Cool"),
    1: ArticleModel(ean=1111, name="Hose", size=35, brand="VeryCool"),
    2: ArticleModel(ean=4444, name="Jacke", size=40, brand="Nice")
}

class Article:
    def get_article_by_id(self, article_id) -> ArticleModel:
        if article_id not in ARTICLES:
            return False
        return ARTICLES[article_id]
    
    def safe_new_article(self, articledata) -> int:
        article_ids = list(ARTICLES.keys())
        new_article_id = max(article_ids) + 1
        ARTICLES.update({new_article_id: articledata})
        return new_article_id
    
    def get_all_articles(self):
        return ARTICLES