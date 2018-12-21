from django.urls import path, include

from .views import ArticleListView, ArticleDetailView, candidate_upload, company_upload, some_view

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('upload-csv/', candidate_upload, name='candidate_upload'),
    path('upload-csv2/', company_upload, name='company_upload')
]
