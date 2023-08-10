from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Recipe, Comment


class UserProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            name='Test User',
            email='testuser@example.com'
        )

    def test_userprofile_creation(self):
        self.assertEqual(self.profile.name, 'Test User')

    def test_str_representation(self):
        self.assertEqual(str(self.profile), 'Test User')


class RecipeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            slug='test-recipe',
            author=self.user,
            instructions='Test instructions'
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')

    def test_number_of_likes(self):
        self.assertEqual(self.recipe.number_of_likes(), 0)

    def test_number_of_comments(self):
        self.assertEqual(self.recipe.number_of_comments(), 0)


class CommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            slug='test-recipe',
            author=self.user,
            instructions='Test instructions'
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            content='Test comment content'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test comment content')

    def test_str_representation(self):
        expected_str = f'Comment by testuser on Test Recipe'
        self.assertEqual(str(self.comment), expected_str)
