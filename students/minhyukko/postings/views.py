import json

from django.views   import View
from django.http    import JsonResponse

from core.utils     import signin_required
from .models        import Post

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
        posts = Post.objects.select_related('posting_user').all()
        results = []
        for post in posts:
            results.append(
                {
                    'user' : post.posting_user.email,
                    'title' : post.title,
                    'image' : post.image,
                    'context' : post.context,
                }
            )
        return JsonResponse({'results': results}, status=200)