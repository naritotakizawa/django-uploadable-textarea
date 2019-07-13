from django import forms
from django.core.files.storage import default_storage
from .models import Post
from .widgets import FileUploadableTextArea


class PostForm(forms.ModelForm):
    """記事の追加フォーム"""

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': FileUploadableTextArea,
        }


class FileUploadForm(forms.Form):
    """ファイルのアップロードフォーム"""
    file = forms.FileField()

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        file_url = default_storage.url(file_name)
        return file_url
