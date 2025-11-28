from django.db import models
from django.contrib.postgres.fields import ArrayField
from uuid import uuid4
import os
import uuid

def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid4().hex}.{ext}'
    return os.path.join(f'{instance.__class__.__name__.lower()}_images', new_filename)

class TeamMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    ROLE_CHOICES = [
        ('DEV', 'Developer'),
        ('DSN', 'Designer'),
        ('PM', 'Project Manager'),
        ('MK', 'Marketing'),
        ('OT', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    bio = models.CharField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=rename_image, blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    skills = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list,
        help_text="List of skills for the team member"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
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
    image = models.ImageField(upload_to=rename_image, blank=True, null=True)
    link = models.URLField(blank=True)
    members = models.ManyToManyField(TeamMember, related_name='projects')
    technologies = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list,
        help_text="List of technologies for the project"
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date', 'title']

    def __str__(self):
        return self.title
    
class WorkExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    member = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='work_experiences'
    )
    
    company_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=rename_image, blank=True, null=True)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company_name}"
    
class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    member = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='educations'
    )
    image = models.ImageField(upload_to=rename_image, blank=True, null=True)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.university}"
    
class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    member = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='achievements'
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=rename_image, blank=True, null=True)
    description = models.TextField(blank=True)
    event = models.CharField(max_length=150, blank=True, help_text="Hackathon, competition, conference name")
    date = models.DateField(blank=True, null=True)
    award = models.CharField(max_length=150, blank=True, help_text="Prize, rank, or award title")
    link = models.URLField(blank=True, help_text="Optional link to certificate or event page")

    class Meta:
        ordering = ['-date', 'title']

    def __str__(self):
        return f"{self.title} - {self.member.full_name}"