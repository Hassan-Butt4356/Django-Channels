import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from myapp.routing import websocket_urlpatterns

from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':URLRouter(
        websocket_urlpatterns
    )
})

# to use authentication in channels we have to use AuthMiddlewareStack and inside we have to provide websockets Urls

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket':AuthMiddlewareStack(
#         URLRouter(
#         websocket_urlpatterns
#     ))
# })

# to check wheter a user is authenticated or not in consumer
# if self.scope['user'].is_authenticated: #it is same as request.user.is_authenticated
#     perform task

# To get user we have to use this
# self.scope['user'] # this is same as request.user
