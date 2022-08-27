from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("saving",views.saving,name="saving"),
    path("listing/<thisid>",views.listing,name="listing"),
    path("biding/<thisid>",views.biding,name="biding"),
    path("comment/<thisid>",views.commenting,name="comment"),
    path("watchlist/",views.watchlist,name="watchlist"),
    path("watchcreate/<thisid>",views.watchcreate,name="watchcreate"),
    path("watchdelete/<thisid>",views.watchdelete,name="watchdelete"),
    path("category/",views.cate,name="category"),
    path("close/<thisid>",views.close,name="close"),
]
