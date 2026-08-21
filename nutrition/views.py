from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile

def home(request):

    if request.method == "POST":

        age = float(request.POST.get("age"))
        gender = request.POST.get("gender")
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        activity = float(request.POST.get("activity"))
        goal = request.POST.get("goal")


        # Convert height from cm to meters
        height_m = height / 100


        # Calculate BMI
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)


        # Calculate BMR
        if gender == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161


        # Calculate maintenance calories
        maintenance_calories = bmr * activity
        maintenance_calories = round(maintenance_calories)


        # Calculate goal-based calories
        if goal == "lose":
            target_calories = maintenance_calories - 300

        elif goal == "gain":
            target_calories = maintenance_calories + 300

        else:
            target_calories = maintenance_calories


        # Send results to HTML
        context = {
            "bmi": bmi,
            "maintenance_calories": maintenance_calories,
            "target_calories": target_calories
        }


        return render(
            request,
            "nutrition/index.html",
            context
        )


    return render(request, "nutrition/index.html")
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):

    return render(
        request,
        "nutrition/index.html"
    )


def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")


        # Check passwords
        if password1 != password2:

            return render(
                request,
                "registration/signup.html",
                {
                    "error": "Passwords do not match."
                }
            )


        # Check username
        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "registration/signup.html",
                {
                    "error": "Username already exists."
                }
            )


        # Create user
        user = User.objects.create_user(

            username=username,

            email=email,

            password=password1

        )


        # Log user in
        login(request, user)


        # Go to homepage
        return redirect("/")


    return render(
        request,
        "registration/signup.html"
    )
def profile(request):

    if not request.user.is_authenticated:

        return redirect("/login/")


    if request.method == "POST":

        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST.get("gender")
        activity_level = request.POST.get("activity_level")
        goal = request.POST.get("goal")
        diet_preference = request.POST.get("diet_preference")
        language = request.POST.get("language")


        Profile.objects.update_or_create(

            user=request.user,

            defaults={

                "age": age,

                "height": height,

                "weight": weight,

                "gender": gender,

                "activity_level": activity_level,

                "goal": goal,

                "diet_preference": diet_preference,

                "language": language,

            }

        )


        return redirect("/")


    return render(
        request,
        "nutrition/profile.html"
    )