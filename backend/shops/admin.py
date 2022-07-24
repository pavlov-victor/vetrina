from django.contrib import admin

from shops.models import MarketTag, Market


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']


@admin.register(MarketTag)
class MarketTagAdmin(admin.ModelAdmin):
    pass
