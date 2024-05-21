from django import template
from django.template.defaultfilters import stringfilter
register= template.Library()

# def cut(value,args):
#     value.replace(args,'')
# register.filter('cut',cut)   

@register.filter
@stringfilter
def cut1(value,arg):
    value.replace(arg,"")


