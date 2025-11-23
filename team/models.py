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


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('WEB', 'Web Development'),
        ('ML', 'Machine Learning'),
        ('DSN', 'Design'),
        ('MKT', 'Marketing'),
        ('OTH', 'Other'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='OTH')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    members = models.ManyToManyField(TeamMember, related_name='projects')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date', 'title']

    def __str__(self):
        return self.title
    
class WorkExperience(models.Model):
    member = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='work_experiences'
    )
    
    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company_name}"