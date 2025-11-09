from django_filters import rest_framework as filters, DataTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DataTimeFromToRangeFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
