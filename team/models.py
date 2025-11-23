from django.db import models

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('DEV', 'Developer'),
        ('DSN', 'Designer'),
        ('PM', 'Project Manager'),
        ('MK', 'Marketing'),
        ('OT', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name
