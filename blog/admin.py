from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdminModel(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']


class TagAdminModel(admin.ModelAdmin):
    raw_id_fields = ['posts']


class CommentAdminModel(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'author',
            'post'
        )

admin.site.register(Post, PostAdminModel)
admin.site.register(Tag, TagAdminModel)
admin.site.register(Comment, CommentAdminModel)
