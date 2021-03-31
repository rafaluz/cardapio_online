from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path('criar_cardapio/', views.MenuCreate.as_view(), name="criar_cardapio"),
    path('meus_cardapios/', views.MenuList.as_view(), name="listar_menu"),
    path('detalhar_cardapio/<int:pk>', views.MenuDetail.as_view(), name='detalhar_menu'),
    path('alterar_menu/<int:pk>', views.MenuUpdate.as_view(), name='alterar_menu'),
    path('deletar_cardapio/<int:pk>', views.MenuDelete.as_view(), name='deletar_menu'),
]
