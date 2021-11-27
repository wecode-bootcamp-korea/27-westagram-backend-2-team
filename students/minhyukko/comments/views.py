import json

from django.http        import JsonResponse
from django.views       import View

from core.utils         import signin_required
from postings.models    import Post
from .models            import Comment

class CommentView(View):
    @signin_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id = data['post'])

            Comment.objects.create(
                post    = post,
                user    = request.user,
                comment = data['comment']
            )

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status = 400)
        
        return JsonResponse({'message':'SUCCESS'}, status=201)

    def get(self, request):
        comments = Comment.objects.select_related('post','user').all()
        results  = []
        for comment in comments:
            results.append(
                {
                    'post'   : comment.post.title,
                    'user'   : comment.user.email,
                    'comment': comment.comment,
                    'created': comment.created_at
                }
            )
        return JsonResponse({'results':results},status=200)
