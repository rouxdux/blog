from django.contrib import admin
from .models import Post
from .models import Knowledge_base
from .models import Faq

# Register your models here.

admin.site.register(Post)
admin.site.register(Knowledge_base)
admin.site.register(Faq)
