from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline_date", "is_done", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "deadline_date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M"
            ),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }