from django.conf import settings
from django.conf.urls import url

from .user.views import AuthenticationGraphQLView

urlpatterns = [
    url(
        r"^graphql",
        AuthenticationGraphQLView.as_view(graphiql=settings.DEBUG),
        name="graphql",
    )
]
