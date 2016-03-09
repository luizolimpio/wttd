from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now

class SubscriptionsModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','cpf','created_at','subcribed_today','paid')
    date_hierarchy = 'created_at'
    search_fields = ('name','email','phone','cpf','created_at')
    list_filter = ('paid','created_at')

    actions = ['mark_as_paid']

    def subcribed_today(self,obj):
        return obj.created_at.date() == now().date()

    subcribed_today.short_description = 'Inscrito hoje?'
    subcribed_today.boolean = True

    def mark_as_paid(self,request,queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = '{} inscrição foi marcada como paga.'.format(count)
        else:
            msg = '{} inscrições foram marcadas como paga.'.format(count)

        self.message_user(request,msg)


    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription,SubscriptionsModelAdmin)


