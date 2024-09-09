from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Push_event)
class PushEventAdmin(admin.ModelAdmin):
    list_display=['author', 'branch', 'datetime']

@admin.register(Pull_request)
class PullRequestAdmin(admin.ModelAdmin):
    list_display=['author', 'from_branch', 'to_branch','datetime']

@admin.register(Merge_event)
class MergeEventAdmin(admin.ModelAdmin):
    list_display=['author', 'from_branch', 'to_branch','datetime']