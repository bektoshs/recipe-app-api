"""
URL mapping for the recipe app.
"""

from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from recipe import views
from .views import RecipeViewSet

router = DefaultRouter()
router.registry('recipes', RecipeViewSet)


app_name = 'recipe'

urlpatters = [
    path('', include(router.urls)),
]