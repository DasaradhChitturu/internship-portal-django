from rest_framework import serializers
from .models import InternshipProgram, InternshipApplication


class InternshipProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternshipProgram

        fields = [
            "id",
            "program_name",
            "duration_months",
            "domain"
        ]
    def validate_program_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Program name must contain at least 3 characters."
            )

        return value

    def validate_duration_months(self, value):
        if value < 1 or value > 12:
            raise serializers.ValidationError(
            "Duration must be between 1 and 12 months."
        )

        return value

    def validate(self, data):
        program_name = data.get("program_name")
        domain = data.get("domain")

        if (
            program_name
            and program_name.lower() == "python backend development"
            and domain != "Software Development"
        ):
            raise serializers.ValidationError(
                "Python Backend Development must belong to Software Development domain."
            )

        return data

class InternshipApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternshipApplication

        fields = [
            "id",
            "student_name",
            "email",
            "status",
            "program"
        ]

        read_only_fields = ["id", "status"]