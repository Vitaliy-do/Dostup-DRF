from rest_framework.permissions import BasePermission

# Класс проверки (аутенфикации) владельца объявления
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Внесено изменение для устранения замечания 1.
        return request.user == obj.creator

