from django.urls import path, register_converter
from crawled_data import views

app_name = 'crawled_data'


urlpatterns = [
    path('', views.crawled_list, name='crawled_list'),                        # 조회
]