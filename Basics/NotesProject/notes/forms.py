from django import forms

from notes.models import Note, Tag


class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']

    def clean_title(self):
        title = self.cleaned_data['title']
        qs = Note.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Note with this title already exists.')
        return title