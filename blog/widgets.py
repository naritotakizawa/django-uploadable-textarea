from django import forms


class ImageUploadableTextArea(forms.Textarea):
    """画像アップロード可能なテキストエリア"""

    class Media:
        js = ['blog/csrf.js', 'blog/upload.js']

    def build_attrs(self, base_attrs, extra_attrs=None):
        if 'class' in base_attrs:
            base_attrs['class'] += ' uploadable vLargeTextField'
        else:
            base_attrs['class'] = 'uploadable vLargeTextField'
        return super().build_attrs(base_attrs, extra_attrs)
