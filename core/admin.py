from django.contrib import admin

# Register your models here.

from .models import User, Nutrition, MealPlan, Workout, Blog, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fat')
    search_fields = ('name',)

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title', 'created_by__username')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title', 'created_by__username')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'created_at')
    search_fields = ('user__username', 'blog__title')
    list_filter = ('created_at',)
    raw_id_fields = ('user', 'blog')
    ordering = ('-created_at',)