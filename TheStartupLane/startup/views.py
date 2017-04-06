from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from models import *

# Create your views here.


def index(request):
    return render_to_response("startup/index.html")


def startups(request):
    startup_list = StartupName.objects.all()
    return render_to_response('startup/startups.html', {'startup_list': startup_list})


def startup_detail(request, startup_name):
    startup = StartupName.objects.get(name=startup_name)
    contact = startup.startupcontact_set.all()
    founder = startup.founder_set.all()
    funding = startup.funding_set.all()
    invested = startup.invested_set.all()

    funding_list = []
    for fund in funding:
        fund.investor = fund.investor.replace('[', '').replace(']', '').split(',')
        fund.funding_date = fund.funding_date.replace('[', '').replace(']', '').split(',')
        fund.amount_round = fund.amount_round.replace('[', '').replace(']', '').split(',')
        fund = zip(fund.investor, fund.funding_date, fund.amount_round)
        funding_list.append(fund)

    invested_list = []
    for invest in invested:
        invest.invested_in = invest.invested_in.replace('[', '').replace(']', '').split(',')
        invest.invested_date = invest.invested_date.replace('[', '').replace(']', '').split(',')
        invest.invested_amount = invest.invested_amount.replace('[', '').replace(']', '').split(',')
        invest = zip(invest.invested_in, invest.invested_date, invest.invested_amount)
        invested_list.append(invest)

    return render_to_response('startup/startup_detail.html', {'startup': startup, 'contacts': contact, 'founders': founder, 'fundings': funding_list, 'invested': invested_list})


def news(request):
    news_list = News.objects.all()
    return render_to_response('startup/news.html', {'news_list': news_list})


def internships(request):
    intern_list = Internship.objects.all()
    return render_to_response('startup/internship.html', {'intern_list': intern_list})


def blog(request):
    return render_to_response('startup/blog.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        if len(query) > 2:
            startup_list = StartupName.objects.filter(name__icontains=query)
            total = startup_list.count()
            return render_to_response('startup/search.html', {'query': query, 'total': total, 'startup_list': startup_list})
        else:
            return render_to_response('startup/search.html', {'error': 'Re-enter query of min. length 3.'})


def city(request, city_name):
    startup_list = StartupName.objects.filter(location=city_name)
    return render_to_response('startup/startups.html', {'startup_list': startup_list})
