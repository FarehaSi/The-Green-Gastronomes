from django.contrib import admin
from .models import Recipe, Comment, UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'content', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        for user_profile in queryset:
            recipes_to_approve = Recipe.objects.filter(author=user_profile.user, approved=False)
            recipes_to_approve.update(approved=True)
        self.message_user(request, f"{queryset.count()} user profiles with recipes approved.")