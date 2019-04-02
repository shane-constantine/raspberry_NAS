from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,FileResponse
from .models import fileModel
from django.utils.encoding import escape_uri_path
from django.http import HttpResponseRedirect
# Create your views here.

def get_file_list_common_data(request,files_all_list):
    context = {}
    context['files'] = files_all_list
    return context

def files_page(request):
    files_all_list = fileModel.objects.all()
    context = get_file_list_common_data(request,files_all_list)
    return render(request,"file_page/file_manage.html",context)

def upload_ajax(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file', None)
        file = fileModel(file=file_obj,path=file_obj.name)
        file.save()
        return HttpResponse('OK')

def download_file(request,pk):
    file_obj = get_object_or_404(fileModel,id=pk)
    filename = file_obj.path.split("/")[-1]
    response = FileResponse(file_obj.file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(filename))
    return response

def delete_file(request,pk):
    file_obj = get_object_or_404(fileModel,id=pk)
    file_obj.delete()
    return HttpResponseRedirect('/files/')