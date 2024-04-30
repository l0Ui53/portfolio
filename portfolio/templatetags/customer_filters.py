from django import template

register = template.Library()

language_colours = {
    'python': 'green',
    'java': 'blue',
    'javascript': 'yellow',
    'ruby': 'red',
    'c++': 'purple'
}

@register.filter(name='colourize') #to register this function as a filter
def colourize(value):
    p_language = value.lower()
    colour = language_colours.get(p_language, 'black')
    colourize = f"<span style='color : {colour}'>{value}</span>"
    return colourize