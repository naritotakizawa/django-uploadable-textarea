from django.http import HttpResponseBadRequest, JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import ImageUploadForm, PostForm
from .models import Post


class PostList(generic.ListView):
    """記事一覧"""
    model = Post


class PostDetail(generic.DetailView):
    """記事詳細"""
    model = Post


class PostAdd(generic.CreateView):
    """記事の追加。実際には、ログイン者だけ使えるようにする、等してください。"""
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')


def upload(request):
    """画像のアップロード用ビュー"""
    form = ImageUploadForm(files=request.FILES)
    if form.is_valid():
        url = form.save()
        return JsonResponse({'url': url})
    return HttpResponseBadRequest()
