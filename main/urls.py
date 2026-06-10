from django.urls import path
from .views import (
    MaqolaList,
    MaqolaDetail,
    BizHaqimizda,
    EskiBlog,
)

urlpatterns = [
    path('', MaqolaList.as_view(), name='royxat'),
    path('<int:pk>/', MaqolaDetail.as_view(), name='detail'),
    path('about/', BizHaqimizda.as_view(), name='about'),
    path('eski-blog/', EskiBlog.as_view(), name='eski_blog'),
]