
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .models import InternshipProgram, InternshipApplication
from .serializers import (
    InternshipProgramSerializer,
    InternshipApplicationSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import SearchFilter

from rest_framework.filters import OrderingFilter

from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .permissions import IsStaffOrReadOnly, IsOwnerOrStaff

import logging

logger = logging.getLogger(__name__)

@login_required(login_url="/login/")
def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Application is running"
    })


def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/health/")

        return render(
            request,
            "core/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "core/login.html")


@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")

    return render(request, "core/logout.html")


@permission_required(
    "core.view_internshipprogram",
    login_url="/login/"
)
def program_list(request):
    programs = InternshipProgram.objects.values(
        "program_name",
        "domain",
        "duration_months"
    )

    return JsonResponse({
        "programs": list(programs)
    })


class ProgramListAPIView(APIView):

    def get(self, request):
        programs = InternshipProgram.objects.all()

        serializer = InternshipProgramSerializer(
            programs,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = InternshipProgramSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProgramListCreateGenericAPIView(ListCreateAPIView):
    queryset = InternshipProgram.objects.all()
    serializer_class = InternshipProgramSerializer

class ProgramDetailGenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InternshipProgram.objects.all()
    serializer_class = InternshipProgramSerializer

class ProgramDetailAPIView(APIView):

    def get(self, request, pk):
        program = get_object_or_404(
            InternshipProgram,
            id=pk
        )

        serializer = InternshipProgramSerializer(program)

        return Response(serializer.data)

    def put(self, request, pk):
        program = get_object_or_404(
            InternshipProgram,
            id=pk
        )

        serializer = InternshipProgramSerializer(
            program,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        program = get_object_or_404(
            InternshipProgram,
            id=pk
        )

        serializer = InternshipProgramSerializer(
            program,
            data=request.data,
            partial=True
    )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        program = get_object_or_404(
        InternshipProgram,
        id=pk
    )

        program.delete()

        return Response(
        status=status.HTTP_204_NO_CONTENT
    )

class ProgramPagination(PageNumberPagination):
    page_size = 2

class ProgramViewSet(ModelViewSet):
    serializer_class = InternshipProgramSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["program_name"]
    ordering_fields = ["program_name", "duration_months"]
    ordering = ["program_name"]
    pagination_class = ProgramPagination

    def get_queryset(self):
        logger.info("Program list requested by user: %s", self.request.user.username)
        queryset = InternshipProgram.objects.all()

        domain = self.request.query_params.get("domain")

        if domain:
            queryset = queryset.filter(domain__iexact=domain)

        return queryset

class ApplicationViewSet(ModelViewSet):

    serializer_class = InternshipApplicationSerializer
    permission_classes = [IsOwnerOrStaff]

    def get_queryset(self):

        # Staff can view all applications
        if self.request.user.is_staff:
            return InternshipApplication.objects.all()

        # Students can view only their applications
        return InternshipApplication.objects.filter(
            student=self.request.user
        )

    def perform_create(self, serializer):

        # Automatically assign the logged-in user
        serializer.save(
            student=self.request.user
        )