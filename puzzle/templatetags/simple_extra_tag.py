from django import template
from puzzle.models import Company, Puzzle
from django.db.models import Count
from accounts.models import Account


register = template.Library()

#count Account
@register.simple_tag
def members():
    return Account.objects.count()

@register.simple_tag
def number_company():
    return Company.objects.count()

@register.simple_tag
def company_with_more_puzzles(count=3):
    return Company.objects.annotate(
        total_puzzles = Count('puzzles')
    ).order_by('-total_puzzles')[:count]

@register.simple_tag
def get_most_popular_puzzle(count=5):
    """
    Później z listy plubień trzeba  zabrać

    """
    return Puzzle.objects.all()[:count]

#pierwsze 100 znaków

