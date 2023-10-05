from django.contrib import admin
from .models import Fruit

class FruitAdmin(admin.ModelAdmin):
    list_display = ['name']  # 관리자 목록 페이지에서 표시할 필드
    search_fields = ['name']  # 검색 기능을 사용하여 검색할 수 있는 필드

admin.site.register(Fruit, FruitAdmin)
