from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Image
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect

from django.urls import reverse



def main(request):
	return render(request, 'shop/main.html')

def about(request):
	return render(request, 'shop/about.html')

def email(request):

	if request.method == 'POST':
		message = request.POST['message']
		gmail = request.POST['gmail']
		send_mail('gmail почта клиента:  ' + gmail, 
		 'Текст сообщения от клиента:  ' + message, 
		 settings.EMAIL_HOST_USER,
		 ['nyazbekovkabyl95@gmail.com'], # <--- вот сдесь ты едешь 2 аккаунт  
		 fail_silently=False)


		messages.success(request, ('Ваша заявка успешно отправлена!'))
		return redirect('email')

	return render(request, 'shop/email.html')




def gallery(request):
	gallery = Image.objects.all()
	return render(request, 'shop/gallery.html', {'gallery':gallery})

def kyrgyzstan(request):
	return render(request, 'shop/kyrgyzstan.html')