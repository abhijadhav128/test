from django.shortcuts import render,HttpResponseRedirect,redirect
from home.models import Task
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login 



# Create your views here.

# class CustomLoginView(LoginView):
#     template_name = 'home/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('tasks')



def home(request):
    context = {'success': False}

    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins  = Task(taskTitle=title ,taskDesc=desc)
        ins.save()
        context = {'success':True}

       
    return render(request,'index.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request,'tasks.html',context)  

def delete_task(request,pk):
    if request.method == 'POST':
        pi = Task.objects.get(id =pk)
        pi.delete()
    return redirect ('/')  
    
def update_view(request,pk):
    if request.method == 'POST':
        pi = Task.objects.get(id=pk)
    return render(request,'update.html',{'pi':pi})    
