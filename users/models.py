from __future__ import unicode_literals

from django.db import models

# Create your models here.

# customization starts here


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class HUserManager(BaseUserManager):
    def create_user(self, **validated_data):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        email = validated_data.get('email')
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')

        user = self.model(
            email = self.normalize_email(email),
            first_name = validated_data.get('first_name', None),
            last_name = validated_data.get('last_name', None),
            gender = validated_data.get('gender', None),
            date_of_birth = validated_data.get('date_of_birth', None),
            height = validated_data.get('height', None),
            weight = validated_data.get('weight', None)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            is_admin = True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class HUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    TITLE_TYPES = (
        ('MRS', 'Mrs'),
        ('MR', 'Mr'),
        ('DR', 'Dr'),
        ('OT', 'Others'),
    )
    title = models.CharField(max_length=5, choices=TITLE_TYPES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    GENDER_TYPES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    date_of_birth = models.DateField(null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = HUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def is_expert(self):
        # The user is identified by their email address
        return self.is_expert

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @classmethod
    def get_by_id(cls, HUser_id):
        return HUser.objects.get(pk=HUser_id)


class CircleManager(models.Manager):

    def create_circle(self, **validated_data):
        """
        Creates and saves circle.
        """

        circle = self.model(
            name = validated_data.get('name', None),
            description = validated_data.get('description', None),
            status = validated_data.get('status', None),
            created_by = validated_data.get('created_by', None),
            max_number_members = validated_data.get('max_number_members', None),
            members_can_refer = validated_data.get('members_can_refer', None),

        )

        circle.save(using=self._db)
        return circle

class Circle(models.Model):


    CIRCLE_STATUS_CHOICES = (
        ('A', 'Active'),
        ('D', 'Deleted'),
    )

    objects = CircleManager()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_by = models.ForeignKey(HUser)
    status = models.CharField(max_length=15, choices=CIRCLE_STATUS_CHOICES,
                              help_text='status of the circle')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first created',)

    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time when customer was last updated',)
    members_can_refer = models.BooleanField(default=False,
                                            help_text='when true, it means '
                                                      'members can bring in other members in to this circle')
    max_number_members = models.SmallIntegerField(default=10, help_text='Maximum allowed number of members in the group')



class CircleMemberManager(models.Manager):

    def create_circlemember(self, **validated_data):
        circlemember = self.model(
            email = validated_data.get('email', None),
            first_name = validated_data.get('first_name', None),
            last_name = validated_data.get('last_name', None),
            invited_by = validated_data.get('invited_by', None),
            role = validated_data.get('role', None),
            status = validated_data.get('status', None),
            creation_timestamp = validated_data.get('creation_timestamp', None),
            last_update_timestamp = validated_data.get('last_update_timestamp', None),
            circle_id = validated_data.get('circle_id', None),
            user_id = validated_data.get('user_id', None),
        )
        circlemember.save(using=self._db)
        return circlemember


class CircleMember(models.Model):
    CIRCLE_MEMBER_STATUS_CHOICES = (
        ('A', 'Active'),
        ('N', 'Not Accepted'),
        ('D', 'Deleted'),
    )
    CIRCLE_MEMBER_ROLE = (
        ('M', 'Manager'),
        ('O', 'Owner'),
        ('U', 'User'),
    )
    objects = CircleMemberManager()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    invited_by = models.ForeignKey(HUser)
    role = models.CharField(max_length=1)
    status = models.CharField(max_length=1, choices=CIRCLE_MEMBER_STATUS_CHOICES,
                              help_text='status of the member in the circle')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first created',)

    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time when customer was last updated',)
    circle_id = models.ForeignKey(Circle)
    user_id = models.IntegerField(null=True)
