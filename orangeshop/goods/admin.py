from django.contrib import admin

# Register your models here.
from .models import Good, ParameterInGood, Parameter, Category


class ParameterInGoonInline(admin.TabularInline):
    model = ParameterInGood
    extra = 1


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seller', 'category')
    list_filter = ('price', 'category')
    search_fields = ('title',)
    inlines = (ParameterInGoonInline,)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'good_count')
    search_fields = ('title', )

    def good_count(self, obj):
        return obj.goods.count()
