from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def endpoints(request):

    data = ['/auth/                   (for login)',
            '/auth/refresh/           (refresh token)',
            '/users/register/         (register user)',
            '/profiles                (list of profiles)',
            '/contents                (list of profiles)',
            '/contents/profile        (contents profile)',]
    
    return Response(data)