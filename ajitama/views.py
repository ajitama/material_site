from material.frontend.views import ModelViewSet
from .import models

# Create your views here.
class ArticleViewSet(ModelViewSet):
    model = models.Article
    ordering = ['-subject', 'data_date']
    list_display = ('subject','data_date', 'data_bool','data_choice')


