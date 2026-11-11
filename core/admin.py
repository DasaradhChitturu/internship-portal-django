from django.contrib import admin
from .models import (
    InternshipProgram,
    InternshipApplication,
    StudentProfile,
    Skill
)


@admin.register(InternshipProgram)
class InternshipProgramAdmin(admin.ModelAdmin):
    list_display = ("program_name", "domain", "duration_months")
    search_fields = ("program_name", "domain")
    list_filter = ("domain", "duration_months")


@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ("student_name", "email", "program", "status")
    search_fields = ("student_name", "email", "program__program_name")
    list_filter = ("status", "program")


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "application",
        "college_name",
        "phone_number",
        "graduation_year"
    )
    search_fields = (
        "application__student_name",
        "college_name",
        "phone_number"
    )
    list_filter = ("graduation_year",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "display_programs")
    search_fields = ("skill_name",)

    @admin.display(description="Internship Programs")
    def display_programs(self, obj):
        return ", ".join(
            program.program_name
            for program in obj.programs.all()
        )