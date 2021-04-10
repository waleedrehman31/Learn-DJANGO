from django.urls import path
from blog.views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleListView
)

app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(), name="Article-list"),
    path('create/', ArticleCreateView.as_view(), name="Article-create"),
    path('<int:id>/', ArticleDetailView.as_view(), name="Article-detail"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="Article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="Article-delete"),

]
