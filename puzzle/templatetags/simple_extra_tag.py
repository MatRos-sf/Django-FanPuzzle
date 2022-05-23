from django import template
from puzzle.models import Company, Puzzle


register = template.Library()

@register.simple_tag
def number_company():
    return Company.objects.count()

@register.simple_tag
def get_most_popular_puzzle(count=5):
    """
    Później z listy plubień trzeba  zabrać

    """
    return Puzzle.objects.all()[:count]