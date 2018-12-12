#-*- coding:utf-8 -*-
from django.http import HttpResponse
#from django.utils import simplejson
import simplejson

__author__ = 'czp'


# decorator json response, it's similar to SpringMVC @ResponseBody
def render_json_response(func):
    def _(*args, **kwargs):
        data = func(*args, **kwargs)
        result = simplejson.dumps(data, ensure_ascii=False)
        return HttpResponse(result, mimetype='application/javascript')
    return _
