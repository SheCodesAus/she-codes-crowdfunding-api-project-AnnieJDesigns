from rest_framework import serializers
from .models import Pledge, Project
from users.serializers import CustomUserSerializer

# class CauseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: Cause
#         fields = ['causes']

#     def create(self, validated_data):
#         return Cause.objects.create(**validated_data)
    
class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    cause = serializers.ChoiceField(choices=Project.CAUSE_CHOICE)
    total_likes = serializers.IntegerField(read_only=True)
    total_pledges = serializers.IntegerField(read_only=True)
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id') #look into this #ReadOnly because you dont want users to modify owners
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data) #unpacking syntax - I want you to take out the dictionary and I want you to hand over the all the keys as an agrument
    
class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)

    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.cause = validated_data.get('cause', instance.cause)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

# class CommentsSerializer(serializers.Serializer):
#     class Meta:
#         model = Comments
#         field = ['id', 'comment', 'project', 'supporter']
#         read_only_fields = ['supporter', 'project']
