from django import forms
from .models import Project,Profile,Rating,Comments

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar','country''comment']
        widgets={
            'color':forms.CheckboxSelectMultiple(),
            'technologies':forms.CheckboxSelectMultiple(),
            'categories':forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['profile','project','overall_score']

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','comment','project_id']
