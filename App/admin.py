from django.contrib import admin
from .models import Quiz, Result

class QuizAdmin(admin.ModelAdmin):
    search_fields = ['question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        # ('Language', {'fields': ['name'],}),
        ('Option 1', {'fields': ['option_1'],}),
        ('Option 2', {'fields': ['option_2'],}),
        ('Option 3', {'fields': ['option_3'],}),
        ('Correct Option', {'fields': ['answer'],}),
        ] 
    
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Result)