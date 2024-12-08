from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['image']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileListSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'stars']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileListSerializer()

    class Meta:
        model = Review
        fields = ['user', 'text', 'date']


class ProductListSerializer(serializers.ModelSerializer):
    owner = UserProfileListSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'photos', 'price', 'owner', 'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class CategorySerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'products']



class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileListSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    category = CategorySimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'check_original',
                  'product_video', 'photos', 'price', 'owner', 'created_date', 'ratings', 'reviews']