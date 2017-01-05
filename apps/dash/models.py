from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
	def register(self,request):
		errors = self.input(request)
		if len(errors) > 0:
			return (False, errors)
		pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = self.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'], email = request.POST['email'], pw_hash=pw_hash)

		return(True, user)

	def login(self,request):
		try:
			user = User.UserManager.get(email=request.POST['email'])
			password = request.POST['password'].encode()
			if bcrypt.hashpw(password, user.pw_hash.encode()):
				return (True, user)
		except ObjectDoesNotExist:
			pass
		return (False, ['Email or Password do not match.'])
	
	def input(self, request):
		errors =[]
		if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
			errors.append("Please include a first and/or last name that is longer than 2 characters")
		if not EMAIL_REGEX.match(request.POST['email']):
			errors.append("Please include a valid email.")
		if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_password']:
			errors.append("Passwords must have at least 8 characters and match.")

		return errors

class QuoteManager(models.Manager):
	def submit(self,request):
		errors = self.inputs(request)
		if len(errors) > 0:
			return (False, errors)
		quote = self.create(quotes = request.POST['quote'], auther = request.POST['author'])
		return (True, quote)
	
	def inputs(self,request):
		errors = []
		if len(request.POST['author']) <3:
			errors.append('Author must have 3 or more characters.')
		if len(request.POST['quote']) < 10:
			errors.append('Quote must be longer than 10 characters.') 
		
		return errors

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	pw_hash = models.CharField(max_length =255)
	created_at = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)
	UserManager = UserManager()

class Quote(models.Model):
	quotes = models.CharField(max_length = 255)
	auther = models.CharField(max_length = 255)
	# users = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	QuoteManager= QuoteManager()

