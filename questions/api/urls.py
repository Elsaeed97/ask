from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register("questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<slug:slug>/answers/", qv.AnswersListAPIView.as_view(),name='create_list'),
    path("questions/<slug:slug>/answer/", qv.AnswerCreateAPIView.as_view(),name='create_answer'),
    path("answers/<int:pk>/", qv.AnswerRUDAPIView.as_view(),name='answer_detail'),
     path("answers/<int:pk>/like/", qv.AnswerLikeAPIView.as_view(),name='answer_like'),


]