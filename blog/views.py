from django.shortcuts import render

def post_list(request):
    # Lógica para obtener una lista de publicaciones y pasarla al template
    return render(request, 'blog/post_list.html', {})
