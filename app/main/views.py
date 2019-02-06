from flask import render_template
from . import main
from ..request import get_sources, get_articles

#  Views


@main.route('/')
def index():
    """
    Function that returns the index page and its data

    Example call
    top_headlines = get_sources('de','business')

    We can also have a get_all() function that gets all the news
    Example call from views would be
    everything
    """
    general_list = get_sources('general')
    business_list = get_sources('business')
    technology_list = get_sources('technology')
    sports_list = get_sources('sports')
    health_list = get_sources('health')
    science_list = get_sources('science')
    entertainment_list = get_sources('entertainment')
    return render_template('index.html', general=general_list, business = business_list,technology=technology_list, sports=sports_list, health=health_list, science=science_list,  entertainment=entertainment_list)
