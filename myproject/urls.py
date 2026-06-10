from django.contrib import admin
from django.urls import path, include

from main.views import MaqolaList, MaqolaDetail, BizHaqimizda, EskiBlog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("maqolalar/", MaqolaList.as_view(), name="maqola_list"),
    path("maqolalar/<int:pk>/", MaqolaDetail.as_view(), name="maqola_detail"),
    path("biz-haqimizda/", BizHaqimizda.as_view(), name="biz_haqimizda"),
    path("eski-blog/", EskiBlog.as_view(), name="eski_blog"),
]