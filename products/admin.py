from django.contrib import admin

from .forms import GoodsItemForm
from .models import (AllowedCombination, CarMark, CarModel, CarEngine, GoodsItem,
                     Goods, Category, Brand)

admin.site.register(CarMark)
admin.site.register(CarModel)
admin.site.register(CarEngine)
admin.site.register(Category)
admin.site.register(Brand)


class GoodsItemInline(admin.TabularInline):
    model = GoodsItem
    form = GoodsItemForm
    extra = 0


class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsItemInline]


admin.site.register(Goods, GoodsAdmin)


class GoodsItemAdmin(admin.ModelAdmin):
    form = GoodsItemForm


admin.site.register(GoodsItem, GoodsItemAdmin)


class AllowedCombinationAdmin(admin.ModelAdmin):
    list_display = ['carmark', 'carmodel', 'carengine', ]


admin.site.register(AllowedCombination, AllowedCombinationAdmin)
