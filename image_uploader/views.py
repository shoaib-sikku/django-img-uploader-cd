from django.shortcuts import redirect, render
from api.models import ImageUploader

# -------------------------------------------------------------------
        
def home(request):
    show = ImageUploader.objects.all()
    if request.method=='POST':
        # img = request.POST.get('file')
        img = request.FILES['file']
        var = ImageUploader(photo=img)
        var.save()
        return redirect('/')
    return render(request,"home.html",{'show':show})
