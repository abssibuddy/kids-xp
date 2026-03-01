from django.contrib import admin

from .models import Child, Quest, Submission, XPTransaction, Reward


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "active")


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ("title", "quest_type", "xp_per_unit", "active")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("child", "quest", "units", "status", "created_at")
    list_filter = ("status", "child")


@admin.register(XPTransaction)
class XPTransactionAdmin(admin.ModelAdmin):
    list_display = ("child", "amount", "reason", "created_at")


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ("name", "required_level", "active")
