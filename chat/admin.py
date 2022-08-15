from django.contrib import admin
from .models import  Room, Chat
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'room','user', 'message', 'timestamp']
