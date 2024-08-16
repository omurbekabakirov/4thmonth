from django.contrib import admin
from post.models import Post, Category, Tags


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'category')
    list_editable = ('title', 'rating', 'category')


admin.site.register(Category)
admin.site.register(Tags)

# Register your models here.
