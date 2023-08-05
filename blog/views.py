from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Recipe, UserProfile as UserProfileModel
from .forms import CommentForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import RecipeForm
from django.utils.text import slugify


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
                "comments": comments,
                "commented": True
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@method_decorator(login_required, name="dispatch")
class UserProfile(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfileModel.objects.get(user=request.user)
        profile_form = UserProfileForm(instance=user_profile)
        return render(
            request,
            "user_profile.html",
            {"user_profile": user_profile, "profile_form": profile_form},
        )

    def post(self, request, *args, **kwargs):
        user_profile = UserProfileModel.objects.get(user=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
        return render(
            request,
            "user_profile.html",
            {"user_profile": user_profile, "profile_form": profile_form},
        )


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            recipe.save()
            messages.success(
                request, 'Recipe added successfully and awaiting admin approval.')
            return redirect('user_profile')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Recipe updated successfully and awaiting admin approval.')
            return redirect('user_profile')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully.')
        return redirect('user_profile')
    return render(request, 'delete_recipe.html', {'recipe': recipe})
