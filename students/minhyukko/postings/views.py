import json

from django.views   import View
from django.http    import JsonResponse

from core.utils     import signin_required
from .models        import Post
from users.models   import User

class PostingView(View):
    @signin_required
    def post(self, request):
        try:
            data = json.loads(request.body)

            Post.objects.create(
                posting_user = request.user,
                title        = data['title'],
                image        = data.get('image'),
                context      = data.get('context')
            )
            return JsonResponse({'message':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

    def get(self, request):
        posts = Post.objects.prefetch_related('user', 'comment_set').all()
        results = []
        for post in posts:
            results.append( # coomprehension으로 처리하는게 좋다.
                {
                    'user'   : post.user.email,
                    'title'  : post.title,
                    'image'  : post.image,
                    'context': post.context,
                    'comment': [{'댓글' : comment.comment, '이름' : comment.user.name} for comment in post.comment_set.all()],
                    'created' : post.created_at
                }
            )
        return JsonResponse({'results': results}, status=200)

# class SearchView(View): # get 으로 처리하는 방법
#     def get(self, request): # request.body 를 가져오는것 자체가 모순
#         try:
#             data    = json.loads(request.body)
#             method  = data.get('method')
#             results = []

#             if method == 'email':
#                 user  = User.objects.get(email = data['email'])
#                 posts = Post.objects.filter(user = user)
#             elif method == 'title':
#                 posts = Post.objects.filter(title__contains=data['title'])
#             elif method == 'context':
#                 posts = Post.objects.filter(context__contains=data['context'])
            
#             for post in posts:
#                 results.append(
#                     {
#                         'user'   : post.user.email,
#                         'title'  : post.title,
#                         'image'  : post.image,
#                         'context': post.context,
#                         'comment': [{'댓글' : comment.comment, '이름' : comment.user.name} for comment in post.comment_set.all()],
#                         'created' : post.created_at
#                     }
#                 )
            
#             return JsonResponse({'results': results}, status = 200)

#         except KeyError:
#             return JsonResponse({'message':'KEY_ERROR'}, status = 400)