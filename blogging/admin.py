from django.contrib import admin
from blogging.models import Post, Category

class CategoryInLine(admin.TabularInline):
    model = Category.post.through
    

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('post',)

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine,]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

