from django.shortcuts import render

def index(request):
    return render(request, 'HomePage.html')
def leaderboard(request):
    return render(request, 'LeaderBoardPage.html')

