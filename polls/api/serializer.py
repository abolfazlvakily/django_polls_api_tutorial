from rest_framework.serializers import ModelSerializer
from polls.models import Question , Uplooaded_images
class PostListSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question_text')
        #fields = '__all__'

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class PostDestroySerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'     # if fields == ('id'), ----->>>>> nooooo
class PostupdSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'     # if fields == ('id'), ----->>>>> ?????

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
class upd_img(ModelSerializer):
    class Meta:
        model = Uplooaded_images
        fields = '__all__'