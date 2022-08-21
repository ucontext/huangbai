from rest_framework import serializers


class ArchiveSerializer(serializers.Serializer):
    work_date = serializers.CharField(max_length=11)
    service_item = serializers.CharField(max_length=30)
    service_addr = serializers.CharField(max_length=10)
    service_content = serializers.CharField(max_length=150)
    person_count = serializers.IntegerField()
    work_number = serializers.CharField(max_length=7)
