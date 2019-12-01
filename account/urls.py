from django.urls import path, re_path, reverse_lazy
from account import views
from django.contrib.auth.views import (
LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
PasswordResetConfirmView, PasswordResetCompleteView)


app_name='account'

urlpatterns = [
    path('', views.home , name = 'home-return'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),

    path('reset-password/', PasswordResetView.as_view(template_name='account/resetpassword.html',
    email_template_name='account/reset_passwd_email.html',
    success_url=reverse_lazy('account:password_reset_done'))
    , name='password_reset'),

    #success_url='password_reset/done/'

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='account/resetpassworddone.html'), name='password_reset_done'),

#     re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)$'
# , PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset-password/confirm/<str:uidb64>/<str:token>',
    PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),

   # <str:uidb64>/<str:token> use "/" betweeen two arguments
   # use reverse_lazy Function in success_url for reversing.

    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]
