# # from django.urls import path
# #
# #
# # app_name = 'polls'
# # urlpatterns = [
# #     path('', views.IndexView.as_view(), name='index'),
# #     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
# #     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
# #     path('<int:question_id>/vote/', views.vote, name='vote'),
# # ]
#
#
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from django.contrib import admin
#
# # Create a router and register our viewsets with it.
# from app import views
#
# router = DefaultRouter()
# router.register(r'users', views.UserViewSet, basename="users")
#
#
# app_name = 'app'
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path(r'', views.IndexView.as_view(), name='index'),
#     #path('admin/', admin.site.urls),
#     #path('', include(router.urls)),
# ]
#
# from django.contrib import admin
# from django.urls import include, path
#
#
#
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter


app_name = 'app'


urlpatterns = [

    #path(r'', IndexView.as_view(), name='index'),
    #path('', EditorChartView.as_view(), name='index')
    #path('', TemplateView.as_view(template_name='app/index.html')),
]