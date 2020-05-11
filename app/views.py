from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def count(request):
    user_text = request.GET.get('textarea')
    len(user_text)
    user_count = len(user_text)

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1], reverse=True)

    context = {
        'user_count': user_count,
        'user_text': user_text,
        'sorted_dict': sorted_dict,
    }
    return render(request, 'count.html',context=context)