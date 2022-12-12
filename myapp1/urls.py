from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login
from .views import index_view, form_view,aula_view, aniade_item_views


# #Con funciones
# urlpatterns = [
#     path("", index_view, name="home"),
# ]

#Con clases
urlpatterns = [
    path("", index_view.as_view()),
    #path("login", form_view, name="login"),
    path("login/<username>", aula_view, name="username"),
    path("login",LoginView.as_view(template_name='index.html'), name = 'portfolios'),
    path("login/<username>/portfolio",aniade_item_views, name="aniade_item"),
]