from django.contrib import admin
from App.models import postpaids,Queries,prepaid,postpayment1,Feedback,prepayment,recs,postrecs
admin.site.register(postpaids)
admin.site.register(postpayment1)
admin.site.register(prepaid)
admin.site.register(prepayment)
admin.site.register(recs)
admin.site.register(postrecs)
admin.site.register(Feedback)
admin.site.register(Queries)
