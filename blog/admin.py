from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at',]

    actions = ['make_draft', 'make_published', 'make_withdrawn',]

    def content_size(self, post):
        return mark_safe('<strong>{}</strong> letters/whitespaces'.format(len(post.content)))
    content_size.short_description = 'letter counts'
    #admin.site.register(Post)

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, 'Changed the status of {} posts to "Published" status.'.format(updated_count))
    make_published.short_description = "Change status to 'Published'"

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, 'Changed the status of {} posts to "Draft" status.'.format(updated_count))
    make_draft.short_description = "Change status to 'Draft'"

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w')
        self.message_user(request, 'Changed the status of {} posts to "Withdrawn" status.'.format(updated_count))
    make_withdrawn.short_description = "Change status to 'Withdrawn'"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass