from django.contrib import admin
from .models import Tag, Category, Blog, SubBlog, Travel, Image, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_blog', 'is_vide')
    fields = ('image', 'sub_blog', 'is_vide')
    list_editable = ('sub_blog',)


class ImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 0


class SubBlugInlineAdmin(admin.StackedInline):
    model = SubBlog
    extra = 0



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [SubBlugInlineAdmin]
    list_display = ('id', 'title', 'slug', 'author', 'views', 'category', 'travel', 'created_date')
    fields = ('title', 'slug', 'author', 'image', 'description', 'category', 'tags', 'travel')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'autor__username')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    list_editable = ('author', 'category', 'travel')


@admin.register(SubBlog)
class SubBlogAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]
    list_display = ('id', 'blog')
    fields = ('blog', 'description',)
    search_fields = ('blog__title',)
    list_editable = ('blog',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'email', 'created_date')
    fields = ('blog', 'name', 'email', 'image', 'message')
    list_editable = ('blog', )
    search_fields = ('name', 'email')
    list_filter = ('created_date', )
    date_hierarchy = 'created_date'
