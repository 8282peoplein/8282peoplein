from django.shortcuts import render

# Create your views here.
from .models import BlogData


def crawled_list(request):
    news = BlogData.objects.all()
    # 키값이 'q'로 지정된 값이 없으면 None이 반환됨
    q = request.GET.get('q', '')  # 'q'로 지정된 값이 없으면 '' 반환
    if q:  # q가 널 아니면 qs에 filter 조건 추가
        news = news.filter(title__icontains=q)
    return render(request, 'crawled_data/crawled_list.html', {
        'crawled_list': news,
        'q': q, })

