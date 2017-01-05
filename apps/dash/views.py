from django.shortcuts import render,redirect
from django.contrib import messages
from models import User, Quote
# Create your views here.

def index(request):
	return render(request, 'dash/index.html')

def login(request):	
	result = User.UserManager.login(request)

	if result[0] == False:
		print_messages(request, result[1])
		return redirect('/')
	return log_user_in(request, result[1])

def register(request):
	result = User.UserManager.register(request)
	if result[0] == False:
		print_messages(request, result[1])
		return redirect('/')
	return log_user_in(request,result[1])


def log_user_in(request, user):
	request.session['user'] = {
		'id' : user.id,
		'first_name' : user.first_name,
		'last_name' : user.last_name,
		'email' : user.email,
}
	return redirect('/quotes')

def logout(request):
	request.session.pop('user')
	return redirect('/')

def quotes(request):
	user = User.UserManager.all()
	quote = Quote.QuoteManager.all()
	context = { 
		"user" : user,
		"quote" :quote	}

	if not 'user' in request.session:
			return redirect('/')
	return render(request, 'dash/quotes.html' , context)

def submit_quote(request):
	result = Quote.QuoteManager.submit(request)
	
	if result[0] == False:
		print_messages(request, result[1])
		return redirect('/quotes')
	return redirect('/quotes', result[1])



def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)

