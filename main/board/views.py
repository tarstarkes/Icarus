from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'board/board.html')
def meetings(request):
	return render(request, 'board/meetings.html')