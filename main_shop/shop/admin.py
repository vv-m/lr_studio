from django.contrib import admin
from .models import User, Category, Product
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ['name', 'slug']
    # Автоматическое создание алиаса (slag)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ('category',)
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

