from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm, LoginForm


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


@login_required
def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                instructions=data.get('instructions'),
                time_required=data.get('time_required'),
                author=data.get('author'),
            )
            return HttpResponseRedirect(reverse("homepage"))
            # return HttpResponseRedirect(reverse("recipeview", args=[new_recipe.id]))

    form = RecipeForm()
    return render(request, "basic_form.html", {"form": form})


@login_required
def author_form_view(request):
    if request.user.is_staff:

        if request.method == "POST":
            form = AuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
                Author.objects.create(name=data.get("username"), user=new_user)
                return HttpResponseRedirect(reverse("homepage"))
    else:
        return HttpResponse("Dont have proper credentials return home")
    form = AuthorForm()
    return render(request, "basic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse("homepage"))
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    form = LoginForm()
    return render(request, "basic_form.html", {"form": form})





def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
