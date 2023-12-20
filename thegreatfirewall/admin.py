from django.contrib import admin
from .models import TicketPS, FqdnPS, IPv4PS, IPv6PS

admin.site.register(TicketPS)
admin.site.register(FqdnPS)
admin.site.register(IPv4PS)
admin.site.register(IPv6PS)

