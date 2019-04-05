from django.shortcuts import render

# Create your views here.
def free_speech(request):
    return render(request, 'post/free_speech.html')

def translation(request):
    return render(request, 'post/translation.html')