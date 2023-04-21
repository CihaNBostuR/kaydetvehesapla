from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import CheckboxData
from django.contrib import messages



def my_view(request):
    if request.method == 'POST':
        selected_options = request.POST.getlist('selected_options')
        if len(selected_options)>5:
            data = CheckboxData()
            data.data = ','.join(selected_options)
            data.save()
            messages.success(request,'Başarıyla kayıt sağlandı,devam et!!!!!!!!!!!')
            return redirect('/boxes/as')
    
    return render(request, 'txt_app/checkbox_form.html')






def save_checkbox_count(request):
    selected_options_count = request.POST.get('selected_options_count', 0)
    checkbox = CheckboxData.objects.first()
    if checkbox:
        checkbox.selected_options = selected_options_count
        checkbox.fee = selected_options_count * 0.25
        checkbox.save()
    else:
        CheckboxData.objects.create(selected_options=selected_options_count, fee=selected_options_count * 0.25)
    return JsonResponse({'success': True})





