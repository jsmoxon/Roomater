from feedback.models import *
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Suggestion)
admin.site.register(Survey)
admin.site.register(Option)