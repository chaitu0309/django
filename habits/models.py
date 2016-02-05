from __future__ import unicode_literals

from django.db import models

# Create your models here.

habit_gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both'),
    )

class HabitManager(models.Manager):

    def create_habit(self, **validated_data):
        """
        Creates and saves circle.
        """

        Habit = self.model(
            name = validated_data.get('name', None),
            short_desc = validated_data.get('short_desc', None),
            text = validated_data.get('text', None),
            status = validated_data.get('status', None),
            is_bad_habit = validated_data.get('is_bad_habit', None),
            suggested_age_lower = validated_data.get('suggested_age_lower', None),
            suggested_age_upper = validated_data.get('suggested_age_upper', None),
            available_to_gender = validated_data.get('available_to_gender', None),
        )

        Habit.save(using=self._db)
        return Habit


class Habit(models.Model):

    habit_status_choices = (
        ('UC', 'UnderConstruction'),
        ('UR', 'UnderReview'),
        ('SU', 'Submitted'),
        ('PU', 'Published'),

    )
    objects = HabitManager()
    name = models.CharField(max_length=50,
                            help_text='name of the habit, ex: Smoking, Overspending, Jogging',)
    short_desc = models.CharField(max_length=500, help_text='brief description of the habit',)
    text = models.TextField(help_text='full text of the habit with risks and benefits applicable',)
    status = models.CharField(max_length=2, choices=habit_status_choices,
                              help_text='different statuses available for habit')
    is_bad_habit = models.BooleanField(default=False, help_text='identifies as bad habit when true',)
    suggested_age_lower = models.SmallIntegerField(help_text='identifies the subscribers lowest eligible age limit',)
    suggested_age_upper = models.SmallIntegerField(help_text='identifies the subscribers upper eligible age limit',)
    available_to_gender = models.CharField(max_length=1,  choices=habit_gender_choices,
                                           help_text='identifies the eligible genders who can subscribe to this habit',)


class HabitServiceManager(models.Manager):

    def create_habitservice(self, **validated_data):
        """
        Creates and saves circle.
        """

        HabitService = self.model(
            habit_id = validated_data.get('habit_id', None),
            user_id = validated_data.get('user_id', None),
            nick_name = validated_data.get('nick_name', None),
            status = validated_data.get('status', None),
            end_date = validated_data.get('end_date', None),
        )

        HabitService.save(using=self._db)
        return HabitService


class HabitService(models.Model):
    habit_service_status_choices = (
        ('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')
    )
    objects = HabitServiceManager()
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE,
                                 help_text='identifies the habit template to which customer subscribed to',
                                 )
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                      help_text='identifies the customer signed up for the habit')
    nick_name = models.CharField(max_length=50, help_text='customer given name for the habit, like "my smoking habit"')
    status = models.CharField(max_length=1, choices=habit_service_status_choices,
                              help_text='status of the habit status')
    end_date = models.DateField(blank=True, help_text='')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first subscribed to this Habit',)

    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time when customer last updated this Habit',)



class HabitReviewManager(models.Manager):

    def create_habitreview(self, **validated_data):
        """
        Creates and saves circle.
        """

        HabitReview = self.model(
            habit_id = validated_data.get('habit_id', None),
            user_id = validated_data.get('user_id', None),
            rating = validated_data.get('rating', None),
            comments = validated_data.get('comments', None),
        )

        HabitReview.save(using=self._db)
        return HabitReview


class HabitReview(models.Model):
    rating_choices = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )
    objects = HabitReviewManager()
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE,
                                 help_text='uniquely identifies the habit')
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                      help_text='identifies the customer who gave the rating and wrote a review',)
    rating = models.SmallIntegerField(choices=rating_choices, help_text='identifies the customers rating',)
    comments = models.TextField(blank=True, help_text='customers review comments',)



