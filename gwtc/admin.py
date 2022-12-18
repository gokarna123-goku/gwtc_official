from django.contrib import admin
from .models import Contact, Portfolio, PortfolioCategory


# Register your models here.
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(PortfolioCategory)