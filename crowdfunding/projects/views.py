from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

# class CauseList(APIView):
#      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#      def get(self, request):
#          causes = Cause.objects.all()
#          serializer = CauseSerializer(causes, many=True)
#          return Response(serializer.data)
     
# class CauseDetail(APIView):
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#      ]

#     def get_object(self,pk):
#          try:
#              causes = Cause.objects.get(pk=pk)
#              self.check_object_permissions(self.request, causes)
#              return Cause.objects.get(pk=pk)
#          except Cause.DoesNotExist:
#              raise Http404
        
#     def get(self, request, pk):
#         causes = self.get_object(pk)
#         serializer = CauseSerializer(causes)
#         return Response(serializer.data)

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user) #when a request comes through it searches for the owner variable 
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
                #return is the end of the logic
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    def get_object(self, pk):
        try: #try and expect are python code. try this but if does not exist go to expectation
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404 #this is called a end point

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PledgeList(generics.ListCreateAPIView):

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)


class Liked(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        if project.liked_by.filter(username=request.user.username).exists():
            project.liked_by.remove(request.user)
        else:
            project.liked_by.add(request.user)
        serializer = ProjectSerializer(instance=project)
        return Response(serializer.data)
    



