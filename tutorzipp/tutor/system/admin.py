from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TutorDetail)


from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
   # list_display=('')
   pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Data)
admin.site.register(tutorreg)
admin.site.register(tutorreg2)
admin.site.register(addtutor)
admin.site.register(Payment)
admin.site.register(attendence)
admin.site.register(notification1)
admin.site.register(personaltutor)
admin.site.register(Room)
admin.site.register(Message)