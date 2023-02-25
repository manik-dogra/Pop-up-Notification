from curses.ascii import US
import imp
from django.contrib import admin

from .models import User

admin.site.register(User)