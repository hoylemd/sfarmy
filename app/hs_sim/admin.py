from django.contrib import admin

from .models import Card, Ability

# Register your models here.
admin.site.register(Card)


class AbilityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ability, AbilityAdmin)
