from django.urls import path
from .views import *
from django.contrib.auth import views

app_name = "accounts"

urlpatterns = [
    path('accounts/usuario_create/', UsuarioCreate.as_view(), name="usuario_create"),
    path('login/', views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    
    # Alterar password
    path('password_change/', views.PasswordChangeView.as_view(
        template_name='usuario/password_change_form.html',
        success_url=reverse_lazy('accounts:password_change_done'),
        ), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(
        template_name='usuario/password_change_done.html',
        ), name='password_change_done'),

    # tela do form para inserir o email
    path('password_reset/', views.PasswordResetView.as_view(
        template_name='usuario/password_reset.html',
        email_template_name='usuario/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done'),
        ), name='password_reset'),
    # tela com mensagem informátiva, após enviar o email.
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='usuario/password_reset_done.html'), name='password_reset_done'),
    # tela do form para inserir a nova senha
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='usuario/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete'),
        ), name='password_reset_confirm'),
    # mensagem final, apos redefinir a senha
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='usuario/password_reset_complete.html'), name='password_reset_complete'),
]
