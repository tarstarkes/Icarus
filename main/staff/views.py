from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'staff/staff.html')
def board(request):
	return render(request, 'staff/board.html')