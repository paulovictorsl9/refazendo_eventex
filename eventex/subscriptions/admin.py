from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'inscrito_hoje', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def inscrito_hoje(self, obj):
        return obj.created_at == now().date()

    inscrito_hoje.short_description = 'inscrito hoje?'
    inscrito_hoje.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin)

