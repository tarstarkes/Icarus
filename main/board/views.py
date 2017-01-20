from django.shortcuts import render
from board.models import *

# Create your views here.
def index(request):
	return render(request, 'board/board.html')
def meetings(request):
	meetingData = EventsBoardmeeting.objects.all().order_by('-date')
	return render(request, 'board/meetings.html', {'data': meetingData })