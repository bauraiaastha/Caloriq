from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    ACTIVITY_CHOICES = [
        ("sedentary", "Sedentary"),
        ("light", "Lightly Active"),
        ("moderate", "Moderately Active"),
        ("active", "Very Active"),
        ("extra", "Extra Active"),
    ]

    GOAL_CHOICES = [
        ("lose", "Lose Weight"),
        ("maintain", "Maintain Weight"),
        ("gain", "Gain Weight"),
    ]

    DIET_CHOICES = [
        ("vegetarian", "Vegetarian"),
        ("non_vegetarian", "Non-Vegetarian"),
        ("vegan", "Vegan"),
    ]

    LANGUAGE_CHOICES = [
        ("english", "English"),
        ("hindi", "हिन्दी"),
        ("bengali", "বাংলা"),
        ("tamil", "தமிழ்"),
        ("telugu", "తెలుగు"),
        ("marathi", "मराठी"),
        ("gujarati", "ગુજરાતી"),
        ("kannada", "ಕನ್ನಡ"),
        ("malayalam", "മലയാളം"),
        ("punjabi", "ਪੰਜਾਬੀ"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    age = models.PositiveIntegerField()

    height = models.FloatField()

    weight = models.FloatField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    activity_level = models.CharField(
        max_length=20,
        choices=ACTIVITY_CHOICES
    )

    goal = models.CharField(
        max_length=10,
        choices=GOAL_CHOICES
    )

    diet_preference = models.CharField(
        max_length=20,
        choices=DIET_CHOICES
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default="english"
    )

    def __str__(self):

        return self.user.username