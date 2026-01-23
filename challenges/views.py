from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'Learn to say \'hello\' in 10 different languages without looking them up twice.',
    'february': 'Write a 4-line poem for every person who makes you a coffee or meal this month.',
    'march': 'Walk backwards for at least 5 minutes every day (safely!) to confuse your pedometer.',
    'april': 'Commit to a \'No-Puns\' week. If you fail, you have to wear your socks mismatched for a day.',
    'may': 'Talk to your houseplants for 2 minutes a day. Document which one seems the most judgmental.',
    'june': 'Eat every meal this month with your non-dominant hand. Mastery or mess—choose one.',
    'july': 'Narrate your life like a nature documentary commentator for 10 minutes every evening.',
    'august': 'Try to recreate a famous painting using only items found in your kitchen junk drawer.',
    'september': 'Communication challenge: Use one \'vintage\' slang word (like \'balderdash\' or \'groovy\') in every meeting.',
    'october': 'Perfect your \'spooky walk\' and use it exclusively whenever you enter a kitchen.',
    'november': 'Write a Yelp-style review for every mundane object you use, like your stapler or a specific spoon.',
    'december': 'Gift-wrap something you already own and give it to yourself on a Tuesday just for the drama.'
}


def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges):
        return HttpResponseNotFound('This month is not supported.')

    redirect_month = list(monthly_challenges.keys())[month - 1]

    redirect_url = reverse('monthly_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except KeyError:
        return HttpResponseNotFound('This month is not supported.')