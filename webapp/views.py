from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views import generic
from .models import Items
from django.urls import reverse_lazy

class homepage(generic.ListView):
    template_name='index.html'
    context_object_name='item_list'
    def get_queryset(self):
        return Items.objects.all()

class ItemsDeleteView(generic.DeleteView):
    model=Items
    success_url=reverse_lazy('appweb:homepage')

def add(request):
    print(request)
    if request.method=='POST':
        itm_name=request.POST['name']
        itm_quantity=request.POST['quantity']
        itm_status=request.POST['status']
        itm_date=request.POST['date']
        if(itm_date=='' or itm_quantity=='' or itm_status=='' or itm_name==''):
            messages.info(request,"PLEASE,ENTER ALL FIELDS")
            return redirect('appweb:add') 
        obj=Items(item_name=itm_name,item_quantity=itm_quantity,item_status=itm_status,date=itm_date)
        obj.save()
        return redirect('appweb:homepage')
    else:
        return render(request, 'add.html')
    


def filter(request):
    if request.method=='POST':
        itm_date=request.POST['date']
        if(itm_date==''):
            messages.info(request,"PLEASE SELECT A VALID DATE")
            return redirect('appweb:homepage')
        else :
            filtered_items=Items.objects.filter(date=itm_date)
            context={'item_list':filtered_items}
            return render(request, 'index.html',context)

def update_redirection(request,item_id):   
    item = Items.objects.get(pk=item_id)
    context={'item':item,}
    return render(request, 'update.html',context)

def delete_add(request,item_id):
    if request.method=='POST':
        itm_date=request.POST['date']
        itm_name=request.POST['name']
        itm_quantity=request.POST['quantity']
        itm_status=request.POST['status']
        all_items=Items.objects.all()
        if(itm_date=='' or itm_quantity=='' or itm_status=='' or itm_name==''):
            messages.info(request,"PLEASE,ENTER ALL FIELDS")
            lnk='/redirect-to-updateform/'+str(item_id)
            return redirect(lnk) 
        else:
            old_obj = get_object_or_404(Items,pk=item_id)
            old_obj.delete()
            obj=Items(item_name=itm_name,item_quantity=itm_quantity,item_status=itm_status,date=itm_date)
            obj.save()
            return redirect('appweb:homepage')
               