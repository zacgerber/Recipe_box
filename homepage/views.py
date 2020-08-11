from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Recipe
from homepage.models import Author
from homepage.forms import RecipeForm, AuthorForm
# Create your views here.


def index(request):
    html = "index.html"
    my_recipes = Recipe.objects.all()
    return render(request, html, {"recipes": my_recipes, "welcome_name": "box"})


def post_detail(request, post_id):
    html = "post_detail.html"
    my_recipes = Recipe.objects.filter(id=post_id).first()
    return render(request, html, {"post": my_recipes})


def author_detail(request, post_id):
    html = "author_detail.html"
    my_author = Author.objects.filter(id=post_id).first()
    my_recipe = Recipe.objects.filter(author=my_author.id)
    return render(request, html, {"post": my_author, "recipes": my_recipe})


def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                author=data.get('author'),
                instructions=data.get('instructions'),
                time_required=data.get('time_required')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = RecipeForm()
    return render(request, "basic_form.html", {"form": form})


def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "basic_form.html", {"form": form})
