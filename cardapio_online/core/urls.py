from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Index, name="index"),
    path('welcome/', views.Welcome, name="welcome"),
]
