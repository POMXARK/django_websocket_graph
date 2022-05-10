from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from app.views import TableViewSetAi1, LoginUser, TableViewSetAi2, logout_user
from djangoProject.views import TemplateView

router = DefaultRouter()

router.register(r'tables-1', TableViewSetAi1, basename='tables-1')
router.register(r'tables-2', TableViewSetAi2, basename='tables-2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='app/index.html'), name='home'),
    path('api/', include(router.urls)),
    path('',LoginUser.as_view(), name='login'),
    path('logout/',logout_user, name='logout'),
    # path('app/', include('app.urls')),
]





