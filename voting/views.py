from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hash
from .function import addSum, calculate, getHash


def vote(request):
    if request.user.is_authenticated:
        return render(request, 'voting/vote.html')
    else:
        return redirect('/')


def process(request, value):
    try:
        if Hash.objects.filter(voter=request.user.username).exists():
            messages.info(request, "Already Voted")
            return redirect('/voting/vote')
    except:
        pass
    if request.user.is_authenticated:
        try:
            prev = Hash.objects.all()[-1].new
        except:
            prev = '6dd24e2f5bbd2c34edc78e6075d3dca41a9a8930679c7adb7fd1f36826956cdf'
        x = getHash(value)
        y = Hash(prev=prev, trans=x[1], new=x[0], voter=request.user.username)
        y.save()
        messages.info(request, 'Voted Sucessfully')
        return render(request, 'voting/vote.html')
    else:
        return redirect('/')


def result(request):
    x = calculate(Hash.objects.all())
    context = {'a': x[0], 'b': x[1], 'c': x[2],
               'd': x[3], 'e': x[4], 'f': x[5]}
    return render(request, 'voting/results.html', context)
