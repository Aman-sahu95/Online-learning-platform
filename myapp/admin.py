from django.contrib import admin
from .models import News, Branch, Course, Session,Study

# Register your models here.
admin.site.register(News)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Study)
