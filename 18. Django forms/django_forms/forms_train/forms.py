from django import forms

class UserForm(forms.Form):

    name = forms.CharField()
    age = forms.IntegerField()
    required_css_class = "field"
    error_css_class = "error"


class SurveyForm(forms.Form):

    favorite_language = forms.ChoiceField(
        label="Улюблена мова програмування",
        choices=[('py', 'Python'), ('js', 'JavaScript'), ('c', 'C')]
    )

    frameworks = forms.MultipleChoiceField(
        label="Знайомі фреймворки",
        choices=[('dj', 'Django'), ('fl', 'Flask'), ('re', 'React')],
        widget=forms.CheckboxSelectMultiple,
    )

    has_experience = forms.BooleanField(
        label="Чи маєте досвід?",
        required=False,
    )

    start_date = forms.DateField(
        label="Дата початку",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )