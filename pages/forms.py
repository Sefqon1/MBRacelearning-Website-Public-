from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

LANGUAGE_LEVELS = [
    ("a1", "A1"),
    ("a2", "A2"),
    ("b1", "B1"),
    ("b2", "B2"),
    ("c1", "C1"),
    ("c2", "C2"),
]

LESSON_DURATION = [
    ("45","45 minutes"),
    ("60","60 minutes"),
    ("90","90 minutes"),
]

PACKAGE = [
    ("1","1 lesson"),
    ("5","5 lessons"),
    ("10", "10 lessons"),
    ("20", "20 lessons"),

]

LESSON_TYPE = [
    ("business","Business English"),
    ("general","General English tutoring"),
    ("editing", "Editing"),
]

TRIAL_LESSON = [
    ("yes","Yes"),
    ("no","No"),
]


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    languagelevel = forms.CharField(
        label="Language level",
        widget=forms.Select(choices=LANGUAGE_LEVELS),
    )
    lessonduration = forms.CharField(
        label="Duration",
        widget=forms.Select(choices=LESSON_DURATION),
    )
    lessonpackage = forms.CharField(
    label="Package",
    widget=forms.Select(choices=PACKAGE),
    )
    lessontype = forms.CharField(
    label="Lesson Type",
    widget=forms.Select(choices=LESSON_TYPE),
    )

    triallesson = forms.ChoiceField(widget=forms.RadioSelect, choices=TRIAL_LESSON)

    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)

