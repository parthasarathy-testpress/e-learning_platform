"""
ASGI config for educa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # 👈 import your chat app’s routing.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')
django.setup()
application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),   # for normal HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # 👈 must exist
        )
    ),
})