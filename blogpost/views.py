from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(ListView):
    template_name = 'detail.html'
    model = BlogModel