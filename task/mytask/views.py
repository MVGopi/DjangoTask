from django.shortcuts import render, redirect
from django.http import HttpResponse
from mytask.models import Data
import random
from task import settings
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
	if request.method == 'POST':
		Email = request.POST['e']
		subject = 'Reg: Account Creation'
		chars = ['a', 'b', '1', '3', '9', 'j', '5', 'k', 'c', '4']
		Password = ''
		for i in range(8):
			Password += random.choice(chars)
		name = Email.split('@')[0] 
		dummylink = 'www.dummylink.com/login'
		message = '''Hi {},\n\nFind the below email and password to access the following\n\nYour email: {}\nYour password: {}\n\n{}\n\nThank You\nM Venkata Gopi'''.format(name, Email, Password, dummylink)
		from_mail = settings.EMAIL_HOST_USER
		try:
			record = Data(email = Email, password = Password, status = 0)
			record.save()
			mail = EmailMessage(subject, message, from_mail, [Email])
			mail.send()
		except:
			obj = Data.objects.get(email = Email)
			if(obj.email==Email and obj.password==request.POST['p']):
				if(obj.status==0):
					return render(request, 'change.html', {'data':obj})
				else:
					return render(request, 'home.html', {'data':obj})
			
	return render(request, 'login.html')

def changePassword(request, email):
	if request.method == 'POST':
		user = Data.objects.get(email=email)
		OP = request.POST['op']
		NP1 = request.POST['np1']
		NP2 = request.POST['np2']
		if(user.password == OP and NP1==NP2):
			user.password = NP2
			user.status = 1
			user.save()
			return redirect('login')

	return render(request, 'change.html')
