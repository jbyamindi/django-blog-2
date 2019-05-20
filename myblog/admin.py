from django.contrib import admin
from myblog.models import Post, Category

admin.site.register(Post)
#admin.site.register(Category)
class PostInline(admin.TabularInline):
    model = Post
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]
