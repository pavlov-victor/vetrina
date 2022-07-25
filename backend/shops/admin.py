from django.contrib import admin

from shops.models import MarketTag, Market, MarketItem


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']


@admin.register(MarketTag)
class MarketTagAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketItem)
class MarketItemAdmin(admin.ModelAdmin):
    pass
