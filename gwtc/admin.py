from django.contrib import admin
from .models import Contact, Portfolio, PortfolioCategory

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['portfolio', 'category', 'published_at']

class AdminPortfolioCategory(admin.ModelAdmin):
    list_display = ['category_name']

class AdminContact(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'message', 'msg_date']


# Register your models here.
admin.site.register(Contact, AdminContact)
admin.site.register(Portfolio, AdminPortfolio)
admin.site.register(PortfolioCategory, AdminPortfolioCategory)