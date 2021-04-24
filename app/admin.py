from django.contrib import admin

from app.models import Favourite, Character, Quote


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user',]
    

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'wikiUrl']
    

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['dialog', 'character']
    
