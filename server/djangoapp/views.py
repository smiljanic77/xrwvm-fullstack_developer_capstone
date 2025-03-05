# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {"userName":""}
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    email = data['email']
    first_name = data['firstName']
    last_name = data['lastName']
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Already Registered"})
    
    # Create user and save to the database
    user = User.objects.create_user(username=username, password=password,
                                  email=email, first_name=first_name,
                                  last_name=last_name)
    user.save()
    
    # Login the user and return the username
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...

def get_cars(request):
    count = CarMake.objects.filter().count()
    logger.info(f"Number of car makes: {count}")
    
    if count == 0:
        logger.info("No car makes found, running initiate()")
        initiate()
        # Check if initiate() actually created the records
        count = CarMake.objects.filter().count()
        logger.info(f"After initiate(), number of car makes: {count}")
    
    car_models = CarModel.objects.select_related('car_make').all()
    logger.info(f"Number of car models: {car_models.count()}")
    
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "Type": car_model.car_type,
            "Year": car_model.year,
            "Price": str(car_model.price)
        })
    
    logger.info(f"Returning {len(cars)} cars")
    return JsonResponse({"CarModels": cars})
