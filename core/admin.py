from django.contrib import admin
from core.models import Extension, Department, User
# Register your models here.
admin.site.register(Extension)
admin.site.register(Department)
admin.site.register(User)

admin.site.site_header = 'Just Call'
admin.site.site_title = 'Just Call Administration'