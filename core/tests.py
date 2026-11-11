from django.test import TestCase
from .models import InternshipProgram
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class InternshipProgramTest(TestCase):

    def test_create_internship_program(self):
        program = InternshipProgram.objects.create(
            program_name="Python Backend Development",
            duration_months=4,
            domain="Software Development"
        )

        self.assertEqual(program.program_name, "Python Backend Development")
        self.assertEqual(program.duration_months, 4)
        self.assertEqual(program.domain, "Software Development")

class ProgramAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.rahul = User.objects.create_user(
            username="rahul",
            password="test123"
        )

        self.admin = User.objects.create_user(
            username="admin",
            password="test123",
            is_staff=True
        )

    def test_student_can_view_programs(self):
        self.client.force_authenticate(user=self.rahul)
        InternshipProgram.objects.create(
            program_name="Python Backend Development",
            duration_months=4,
            domain="Software Development"
        )

        response = self.client.get("/api/programs-viewset/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)
        self.assertEqual(
        response.data["results"][0]["program_name"],
        "Python Backend Development"
        )

    def test_student_cannot_create_program(self):
        self.client.force_authenticate(user=self.rahul)

        response = self.client.post(
            "/api/programs-viewset/",
            {
                "program_name": "Java Backend Development",
                "duration_months": 4,
                "domain": "Software Development"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 403)

    def test_staff_can_create_program(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(
            "/api/programs-viewset/",
            {
                "program_name": "Java Backend Development",
                "duration_months": 4,
                "domain": "Software Development"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["program_name"],
            "Java Backend Development"
        )

        self.assertEqual(response.data["duration_months"], 4)

    def test_unauthenticated_user_cannot_view_programs(self):
        self.client.force_authenticate(user=None)

        response = self.client.get("/api/programs-viewset/")

        self.assertEqual(response.status_code, 401)

    def test_missing_application_returns_404(self):
        self.client.force_authenticate(user=self.rahul)

        response = self.client.get("/api/applications/99999/")

        self.assertEqual(response.status_code, 404)

    def test_staff_cannot_create_program_with_invalid_duration(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(
            "/api/programs-viewset/",
            {
                "program_name": "Java Backend Development",
                "duration_months": 15,
                "domain": "Software Development"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("duration_months", response.data)
        self.assertEqual(
            response.data["duration_months"][0],
            "Duration must be between 1 and 12 months."
        )