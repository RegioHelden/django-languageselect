# -*- coding: UTF-8 -*-

from django import template

register = template.Library()
@register.inclusion_tag('languageselect/layer.html', takes_context=True)
def languageselect(context):
    context.update({
        'next': context['request'].path_info
    })

    return context
