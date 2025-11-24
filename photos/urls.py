from django.urls import  path
from photos import views
urlpatterns = [
    path("home", views.GalleryView.as_view(), name="gallery"),
    path("photos/<int:pk>", views.PhotosView.as_view(), name="photos"),
    path("addphotos",views.AddPhotosView.as_view(), name="add_photos"),
]


# 媒体文件配置
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)