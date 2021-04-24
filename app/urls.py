from django.urls import path

from app import views


urlpatterns = [
    path('characters', views.CharacterView.as_view(), name='character'),
    path('characters/<str:id>/quotes', views.CharacterQuoteView.as_view(), name='character_quote'),
    path('characters/<str:character_id>/favorites', views.FavouriteCharacterQuoteView.as_view(), name='favourite_character'),
    path('characters/<str:character_id>/quotes/<str:quote_id>/favorites', views.FavouriteCharacterQuoteView.as_view(), name='favourite_character_quote'),
    path('favorites', views.FavouriteCharacterQuoteView.as_view(), name='favorite'),

]