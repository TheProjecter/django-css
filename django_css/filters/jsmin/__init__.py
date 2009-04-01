from django_css.filters.jsmin.jsmin import jsmin
from django_css.filter_base import FilterBase

class JSMinFilter(FilterBase):
    def filter_js(self, js):
        return jsmin(js)
