from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # Внесено изменение для устранения замечания 3.
    created_at = DateTimeFromToRangeFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
