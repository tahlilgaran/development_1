# from django.contrib.auth.models import User
# from django.db import models
#
# # Create your models here.
# from django.forms import ModelForm
#
#
# CHOICES = (('1', 'عالی',), ('2', 'خوب',),('1', 'متوسط',), ('2', 'بد',),('1', 'خیلی بد',))
#
# class OnlineComment(models.Model):
#     user = models.OneToOneField(User)
#     #tour = models.OneToOneField(Tour) #todo
#     body = models.CharField()
#     date = models.DateTimeField()
#
#     def __str__(self):
#         return "{}".format(self.user.last_name+"-"+self.tour) #todo
#
#
#
# class RatingComment(models.Model):
#     user = models.OneToOneField(User)
#     #tour = models.OneToOneField(Tour) #todo
#     Q1 = models.ChoiceField(widget=models.RadioSelect, choices=CHOICES)
#     Q2 = models.ChoiceField(widget=models.RadioSelect, choices=CHOICES)
#     Q3 = models.ChoiceField(widget=models.RadioSelect, choices=CHOICES)
#     Q4 = models.ChoiceField(widget=models.RadioSelect, choices=CHOICES)
#     Q5 = models.ChoiceField(widget=models.RadioSelect, choices=CHOICES)
#     date = models.DateTimeField()
#
#     def __str__(self):
#         return "{}".format(self.user.last_name+"-"+self.tour) #todo
#
#
# class OnlineCommentForm(ModelForm):
#     class Meta:
#         model = OnlineComment
#         fields = ['body']
#
# class RatingCommentForm(ModelForm):
#     class Meta:
#         model = RatingComment
#         fields = ['Q1','Q2','Q3','Q4','Q5']
#
#
