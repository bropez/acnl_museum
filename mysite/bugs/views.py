from django.shortcuts import render
from django.views import generic

from . import models


class BugList(generic.ListView):
    model = models.Bug