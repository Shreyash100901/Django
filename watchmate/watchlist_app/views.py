# from django.shortcuts import get_object_or_404, render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values('name', 'description', 'active'))
#     }
#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie=Movie.objects.get(pk=pk)
#     data={
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)