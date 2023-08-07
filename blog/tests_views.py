from django.urls import reverse, resolve
from django.test import TestCase
from . import views


class URLTests(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.RecipeList)

    def test_add_recipe_url_resolves(self):
        url = reverse('add_recipe')
        self.assertEquals(resolve(url).func, views.add_recipe)

    def test_edit_recipe_url_resolves(self):
        url = reverse('edit_recipe', args=[1])
        self.assertEquals(resolve(url).func, views.edit_recipe)

    def test_delete_recipe_url_resolves(self):
        url = reverse('delete_recipe', args=[1])
        self.assertEquals(resolve(url).func, views.delete_recipe)

    def test_recipe_like_url_resolves(self):
        url = reverse('recipe_like', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.RecipeLike)

    def test_user_profile_url_resolves(self):
        url = reverse('user_profile')
        self.assertEquals(resolve(url).func.view_class, views.UserProfile)

    def test_recipe_detail_url_resolves(self):
        url = reverse('recipe_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, views.RecipeDetail)
