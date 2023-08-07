# from django.test import TestCase
# from .forms import CommentForm, UserProfileForm, RecipeForm


# class CommentFormTest(TestCase):

#     def test_comment_form_valid_data(self):
#         form = CommentForm(data={'content': 'This is a test comment'})
#         self.assertTrue(form.is_valid())

#     def test_comment_form_no_data(self):
#         form = CommentForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 1)


# class UserProfileFormTest(TestCase):

#     def test_userprofile_form_valid_data(self):
#         form = UserProfileForm(data={
#             'name': 'John Doe',
#             'email': 'john@example.com',
#             'profile_picture': 'path/to/image.jpg'
#         })
#         self.assertTrue(form.is_valid())

#     def test_userprofile_form_no_data(self):
#         form = UserProfileForm(data={
#             'name': '',
#             'email': '',
#         })
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)


# class RecipeFormTest(TestCase):

#     def test_recipe_form_valid_data(self):
#         form = RecipeForm(data={
#             'title': 'Test Recipe',
#             'excerpt': 'This is a test excerpt',
#             'instructions': 'This is how you make it',
#             'featured_image': 'path/to/recipe/image.jpg'
#         })
#         self.assertTrue(form.is_valid())

#     def test_recipe_form_no_data(self):
#         form = RecipeForm(data={
#             'title': '',
#             'excerpt': '',
#             'instructions': '',
#         })
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 3)
