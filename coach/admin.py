from django.contrib import admin
from .models import Tplan, Profile, SiteAdmin, Coaches, TeamTplan


admin.site.register(Tplan)
admin.site.register(TeamTplan)
admin.site.register(Profile)
admin.site.register(SiteAdmin)
admin.site.register(Coaches)
