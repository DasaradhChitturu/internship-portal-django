
from django.db import models
from django.contrib.auth.models import User

class InternshipProgram(models.Model):
    program_name = models.CharField(max_length=100)
    duration_months = models.IntegerField()
    domain = models.CharField(max_length=100)
    def __str__(self):
        return self.program_name

class InternshipApplication(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=20, default="Pending")

    student = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="applications",
    null=True,
    blank=True
)

    program = models.ForeignKey(
        InternshipProgram,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    def __str__(self):
        return f"{self.student_name} - {self.program.program_name}"

class StudentProfile(models.Model):
    application = models.OneToOneField(
        InternshipApplication,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    college_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    graduation_year = models.IntegerField()
    linkedin_profile = models.URLField(blank=True)

    def __str__(self):
        return self.application.student_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    programs = models.ManyToManyField(
        InternshipProgram,
        related_name="skills"
    )

    def __str__(self):
        return self.skill_name