from django.shortcuts import render
from django.views import generic

from . import models


class FishList(generic.ListView):
    model = models.Fish
