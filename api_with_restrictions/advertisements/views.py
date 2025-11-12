from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissoins import IsOwnerOrReadOnly





class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    # Внесено изменение для устранения замечания 6.
    filterset_class = ["status", "creator", "created_at" ]
    # Внесено изменение для устранения замечания 4.
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        # Внесено изменение для устранения замечания 5.
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["destroy", "update", "partial_update"]:
            return [IsOwnerOrReadOnly()]

