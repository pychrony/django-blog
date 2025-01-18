# a new import
from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration
# admin.site.register(Post)
# admin.site.register(Category)


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ("title", "author", "created_date", "published_date")
    list_filter = ("author", "categories", "created_date")
    search_fields = ("title", "text")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
    list_display = ("name", "description")
    search_fields = ("name",)
