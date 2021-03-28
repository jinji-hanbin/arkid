from .base import BaseViewSet
from api.v1.serializers.external_idp import (
    ExternalIdpSerializer,
    ExternalIdpListSerializer,
)
from runtime import get_app_runtime
from django.http.response import JsonResponse
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from common.paginator import DefaultListPaginator
from .base import BaseViewSet
from external_idp.models import ExternalIdp

ExternalIdpPolymorphicProxySerializer = PolymorphicProxySerializer(
    component_name='ExternalIdpPolymorphicProxySerializer',
    serializers=get_app_runtime().external_idp_serializers,
    resource_type_field_name='type'
)

@extend_schema(
    tags = ['external_idp']
)
class ExternalIdpViewSet(BaseViewSet):

    model = ExternalIdp

    serializer_class = ExternalIdpSerializer
    pagination_class = DefaultListPaginator

    def get_queryset(self):
        context = self.get_serializer_context()
        tenant = context['tenant']

        kwargs = {
            'tenant': tenant,
        }

        return ExternalIdp.valid_objects.filter(**kwargs).order_by('id')

    def get_object(self):
        context = self.get_serializer_context()
        tenant = context['tenant']

        kwargs = {
            'tenant': tenant,
            'uuid': self.kwargs['pk'],
        }

        obj = ExternalIdp.valid_objects.filter(**kwargs).first()
        return obj

    @extend_schema(
        responses=ExternalIdpListSerializer
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=ExternalIdpPolymorphicProxySerializer,
        responses=ExternalIdpPolymorphicProxySerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        request=ExternalIdpPolymorphicProxySerializer,
        responses=ExternalIdpPolymorphicProxySerializer,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses=ExternalIdpPolymorphicProxySerializer
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)