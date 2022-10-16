from django.contrib import admin
from .models import User, Category, Product
from mptt.admin import DraggableMPTTAdmin
from .logger import *


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ['name', 'slug']
    # Автоматическое создание алиаса (slag)
    prepopulated_fields = {'slug': ('name',)}


class SubCategoryFilter(admin.SimpleListFilter):
    title = 'Модель автомобиля'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'filter_category'

    def lookups(self, request, model_admin):
        sub_categories = Category.objects.filter(level=1)
        sub_categories_tuple = []
        for cat in sub_categories:
            sub_categories_tuple.append((cat.name, cat.name))
        sub_categories_tuple = tuple(sub_categories_tuple)
        return sub_categories_tuple

    def queryset(self, request, queryset):
        if self.value() is not None:
            current_category = Category.objects.get(name=self.value())
            id_current_category = current_category.id
            logger.debug(queryset)
            return queryset.filter(category=id_current_category)
        else:
            return queryset


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = (SubCategoryFilter,)
    # list_filter = ('category',)
    # Автоматическое создание алиаса (slag)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(User)
admin.site.register(Category, CategoryAdmin,
                    list_display=(
                        'tree_actions',
                        'indented_title',
                        # ...more fields if you feel like it...
                    ),
                    list_display_links=(
                        'indented_title',
                    )
                    )
admin.site.register(Product, ProductAdmin)

