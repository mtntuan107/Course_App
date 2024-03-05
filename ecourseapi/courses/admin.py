from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Category, Course, User, Lesson, Interaction
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class CMTForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

class MyCourseAdmin(admin.ModelAdmin):
    form = CMTForm


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson)
admin.site.register(User)

