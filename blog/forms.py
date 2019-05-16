from django import forms
from django.core.files.storage import default_storage
from .models import Post
from .widgets import ImageUploadableTextArea


class PostForm(forms.ModelForm):
    """記事の追加フォーム"""

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': ImageUploadableTextArea,
        }


class ImageUploadForm(forms.Form):
    """画像のアップロードフォーム"""
    file = forms.ImageField()

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        file_url = default_storage.url(file_name)
        return f'<img src="{file_url}">'
