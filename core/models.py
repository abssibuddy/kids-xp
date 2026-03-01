from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    pin = models.CharField(max_length=16)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Quest(models.Model):
    MINUTES = "minutes"
    PAGES = "pages"
    COMPLETE = "complete"
    TYPE_CHOICES = [
        (MINUTES, "Minutes"),
        (PAGES, "Pages"),
        (COMPLETE, "Complete"),
    ]

    title = models.CharField(max_length=120)
    quest_type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    xp_per_unit = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Submission(models.Model):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    ]

    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.PROTECT)
    units = models.PositiveIntegerField(default=0)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.child} - {self.quest} ({self.status})"


class XPTransaction(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reason = models.CharField(max_length=200)
    submission = models.OneToOneField(Submission, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Reward(models.Model):
    name = models.CharField(max_length=120)
    required_level = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
