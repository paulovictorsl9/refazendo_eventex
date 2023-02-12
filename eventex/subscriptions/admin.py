from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'inscrito_hoje', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ('paid', 'created_at')

    def inscrito_hoje(self, obj):
        return obj.created_at == now().date()

    inscrito_hoje.short_description = 'inscrito hoje?'
    inscrito_hoje.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)

