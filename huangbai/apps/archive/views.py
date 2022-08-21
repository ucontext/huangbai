from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Archive
from .serializers import ArchiveSerializer


class ArchiveView(APIView):
    def get(self, request):
        aqfw_list = Archive.objects.all()
        serializer = ArchiveSerializer(instance=aqfw_list, many=True)
        return Response(serializer.data)
