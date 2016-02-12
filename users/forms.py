from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from material import *
import datetime

from django.template import Template
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10
from material.fields import FormSetField

class LoginForm(forms.Form):

    email = forms.EmailField(
        label = "email",
        max_length = 255,
        required = True
    )

    password = forms.CharField(
        label = "password",
        max_length = 20,
        required = True,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id_login_form"
        self.helper.form_class = "form_class"
        self.helper.form_method = "post"
        self.helper.form_action = "#"

        self.helper.add_input(Submit("submit", "Login"))

CARDIOVASCULAR_RISK_CHOICES =()
APNIA_RISK_CHOICES =()

QUESTION_CHOICES = ()

class RegistrationForm(forms.Form):
    class EmergencyContractForm(forms.Form):
        name = forms.CharField()
        relationship = forms.CharField()
        daytime_phone = forms.CharField()
        evening_phone = forms.CharField(required=False)

    registration_date = forms.DateField(initial=datetime.date.today)
    full_name = forms.CharField()
    birth_date = forms.DateField()
    height = forms.IntegerField(help_text='cm')
    weight = forms.IntegerField(help_text='kg')
    primary_care_physician = forms.CharField()
    date_of_last_appointment = forms.DateField()
    home_phone = forms.CharField()
    work_phone = forms.CharField(required=False)

    procedural_questions = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, required=False,
        choices=QUESTION_CHOICES)

    cardiovascular_risks = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, required=False,
        choices=CARDIOVASCULAR_RISK_CHOICES)

    apnia_risks = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, required=False,
        choices=APNIA_RISK_CHOICES)


    layout = Layout(Row(Column('full_name', 'birth_date',
                               Row('height', 'weight'), span_columns=3), 'registration_date'),
                    Row(Span3('primary_care_physician'), 'date_of_last_appointment'),
                    Row('home_phone', 'work_phone'),
                    Fieldset('Procedural Questions', 'procedural_questions'),
                    Fieldset('Clinical Predictores of Cardiovascular Risk', 'cardiovascular_risks'),
                    Fieldset('Clinical Predictors of sleep Apnia Risk', 'apnia_risks'),
                    Fieldset('Emergence Numbers', 'emergency_numbers'))



class RegistrationForm1(forms.Form):

    email = forms.EmailField(max_length=255)
    password1 = forms.CharField(max_length = 20, required = True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, required = True, widget=forms.PasswordInput())

    TITLE_TYPES = (
        ('MRS', 'Mrs'),
        ('MR', 'Mr'),
        ('DR', 'Dr'),
        ('OT', 'Others'),
    )
    title = forms.ChoiceField(choices=TITLE_TYPES)
    first_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    gender = forms.ChoiceField(
        choices = (
                    ('F', 'Female'),
                    ('M', 'Male'),
                    ('O', 'Other'),
        ),
        widget = forms.RadioSelect,
        initial = 'M',
    )
    date_of_birth = forms.DateField(input_formats=['%d-%m-%Y'], required=False)
    height = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = "id_login_form"
    #     self.helper.form_class = "form_class"
    #     self.helper.form_method = "post"
    #     self.helper.form_action = "#"

    #     self.helper.add_input(Submit("submit", "Save"))