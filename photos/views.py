from django.shortcuts import render,redirect
from django.views import View
from unicodedata import category

from photos.models import Photo,Category
from photos.form import PhotoForm


class GalleryView(View):
    # 分类的业务逻辑，拿取前端分类字段，如果没有这个字段就拿取所有数据返给前端
    # 有这个字段就使用[category__字段名] 去数据库中拿取对应字段，并返回数据给前端
    def get(self, request):
        # 获取当前用户选择的类
        category = request.GET.get('category')
        if category is None:
            photo = Photo.objects.all()
        else:
            photo = Photo.objects.filter(category__photos_name=category)

        categorys = Category.objects.all()
        context = {
            'photos': photo,
            'cate': categorys,
        }
        return render(request, "photos/Gallery.html", context)


class AddPhotosView(View):

    def get(self, request):
        data = Category.objects.all()
        context = {'data': data}
        return render(request, "photos/AddPhotos.html", context)

    def post(self, request):
        # request.POST获取用户前端提交的数据,request.FILES用于接受用户上传的文件
        photo_form = PhotoForm(request.POST, request.FILES)

        # 分类检测
        category_new = request.POST.get('category_new')
        category_id = request.POST.get('category')
        descriptions = request.POST.get('description')

        # 处理新分类的创建
        if category_new:
            category_obj, created = Category.objects.get_or_create(photos_name=category_new)
            # 更新photo_form中的category字段
            photo_form.instance.category = category_obj
        elif category_id:
            try:
                category_obj = Category.objects.get(id=category_id)
                photo_form.instance.category = category_obj
            except Category.DoesNotExist:
                data = Category.objects.all()
                context = {
                    'mes': '选择的分类不存在',
                    'data': data,
                    'photo_form': photo_form,
                    'errors': photo_form.errors,
                }
                return render(request, "photos/AddPhotos.html", context)

        # 表单数据的提交
        if photo_form.is_valid():
            photo_form.save()
            return redirect("gallery")
        else:
            data = Category.objects.all()
            context = {
                'mes': '上传失败',
                'data': data,
                'photo_form': photo_form,
                'errors': photo_form.errors,
            }
            print('错误信息:%s', photo_form.errors)
            return render(request, "photos/AddPhotos.html", context)


class PhotosView(View):

    def get(self, request, pk):

        photo = Photo.objects.get(id=pk)

        # 获取当前图片在相册中的前后图片

        all_photos = Photo.objects.all()

        current_index = list(all_photos).index(photo)

        prev_photo = all_photos[current_index - 1] if current_index > 0 else None

        next_photo = all_photos[current_index + 1] if current_index < len(all_photos) - 1 else None

        

        context = {

            'photos': photo,

            'prev_photo': prev_photo,

            'next_photo': next_photo,

        }



        return render(request, "photos/Photos.html", context)