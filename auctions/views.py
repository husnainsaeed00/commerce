from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect

from .models import User, Category, Listing


def index(request):
    activeListing = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html",{
        "listings": activeListing
    })

def createListing(request):
    if request.method == "GET":
        # Handle the form submission
        # ...
        allCategories = Category.objects.all()

        return render(request, "auctions/create.html", {
            "categories": allCategories
        })
    else:
        # Get the data from the form
        title = request.POST['title']
        description = request.POST['description']
        imageurl = request.POST['imageurl']
        price = request.POST['price']
        category = request.POST['category']
        # We can know who the user is
        currentUser = request.user
        # Get all the content about the particular category
        categoryData = Category.objects.get(categoryName=category)
        # Create a new listing object
        newListing = Listing(
            title=title,
            description=description,
            imageurl=imageurl,
            price=float(price),
            category=categoryData,
            owner=currentUser
        )
        # Insert that object into our database
        newListing.save()
        # Redirect to the index page
        return HttpResponseRedirect(reverse('index'))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
