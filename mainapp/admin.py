from django.contrib import admin


from mainapp import models as mainapp_models

@admin.register(mainapp_models.Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ["name", "description", "price"]