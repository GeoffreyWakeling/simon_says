from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest

from .models import Game, generate_pattern

"""
User hits
/newgame
server responds with redirect to gameID URL
/game/<id>
browser goes to /game/<id>
server responds with full sequence of colors, browser plays full game until
user remembers incorrectly, then
POST score  /game/<id>
"""

# Create your views here.
def index(request):
    return HttpResponseRedirect('/simonsays/newgame')

def newgame(request):
    # this is bad, jsut a placeholder until real authentication is in place
    user = authenticate(username='admin', password='admin')

    game = Game()
    game.sequence = generate_pattern()
    game.player = request.user
    game.save()
    return HttpResponseRedirect('/simonsays/game/%s' % game.id)

def game(request, game_id):
    # check if POST request
    if request.POST:
        score = request.POST.get('score', None)
        if score:
            game = Game.objects.get(id=game_id)
            game.score = score
            game.save()
            return HttpResponse('Score %s saved for game id %s' % (score, game_id))
        else:
            return HttpResponseBadRequest('POST request, but no score found')
    else:
        game = get_object_or_404(Game, pk=game_id)
        return JsonResponse({'sequence': game.sequence})

