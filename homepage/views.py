from django.shortcuts import render

from homepage.models import Recipe
from homepage.models import Author

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
