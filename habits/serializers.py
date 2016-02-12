from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Habit, HabitReview, HabitService


class HabitListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('id', 'name', 'short_desc', 'text', 'status', 'is_bad_habit', 'suggested_age_lower',
                  'suggested_age_upper', 'available_to_gender')

        def create(self, validated_data):
            print "Create......."
            return Habit.objects.create(**validated_data)


class HabitServiceListSerializer():

    class Meta:
        model = HabitService
        fields = ('id', 'habit_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp')

        def create(self, validated_data):
            print "Create......."
            return HabitService.objects.create(**validated_data)


class HabitServiceUpdateSerializer():

    class Meta:
        model = HabitService
        fields = ('id', 'nick_name', 'status', 'end_date')
        lookup_field = ('id')
        read_only_fields = ('creation_timestamp', )

        def update(self, instance, validated_data):
            instance.nick_name = validated_data.get('nick_name', instance.nick_name)
            instance.status = validated_data.get('status', instance.status)
            instance.end_date = validated_data.get('end_date', instance.end_date)


class HabitReviewListSerializer():

    class Meta:
        model = HabitReview
        fields = ('id', 'habit_id', 'user_id', 'rating', 'comments')

        def create(self, validated_data):
            print "Create......."
            return HabitReview.objects.create(**validated_data)