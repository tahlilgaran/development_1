from django.contrib import admin

from quality_control.models import OnlineComment\
    #, RatingComment


class OnlineCommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(OnlineComment, OnlineCommentAdmin)
#
#class RatingCommentAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(RatingComment, RatingCommentAdmin)