from django import forms


class ImageUploadableTextArea(forms.Textarea):
    """画像アップロード可能なテキストエリア"""

    class Media:
        js = ['blog/csrf.js', 'blog/upload.js']

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += ' uploadable vLargeTextField'
        else:
            self.attrs['class'] = 'uploadable vLargeTextField'
