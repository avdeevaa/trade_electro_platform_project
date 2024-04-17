from django.contrib import admin
from django.urls import path, include


# schema_view = get_schema_view(
#     openapi.Info(
#         title="API Documentation for DRF project Educational Modules",
#         default_version='v1',
#         description="DRF project Educational Modules",
#         terms_of_service="https://www.example.com/policies/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seller.urls', namespace='seller')),
    path('users/', include('users.urls', namespace='users')),

    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]