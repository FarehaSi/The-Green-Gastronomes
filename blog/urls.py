from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('user/profile/', views.UserProfile.as_view(), name='user_profile'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]