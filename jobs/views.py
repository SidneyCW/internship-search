from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by("-date_posted")
    serializer_class = JobSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def personalized(self, request):
        profile = request.user.studentprofile
        skills = profile.skills.split(",") if profile.skills else []

        query = Q()
        for skill in skills:
            skill = skill.strip()
            query |= Q(description__icontains=skill) | Q(title__icontains=skill)

        jobs = Job.objects.filter(query).distinct()
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)
