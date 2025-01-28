from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_datatables.filters import DatatablesFilterBackend
from django.contrib.auth.decorators import login_required
from django_require_login.decorators import public
from django.utils.decorators import method_decorator
from django.views.generic import View
from django_require_login.mixins import PublicViewMixin
from .models import Vlans, CoreSubnets
from .serializers import VlansSerializer, CoreSubnetsSerializer

@login_required
def index(request):
    return render(request, 'vlans/vlans.html')

@login_required
def home(request):
    return render(request, 'vlans/home.html')

@login_required
def redirect_to_vlans(request):
    return redirect('vlans')

@login_required
def redirect_to_coresubnets(request):
    return redirect('coresubnets')

@login_required
def coresubnets(request):
    return render(request, 'vlans/coresubnets.html')

@public
def my_public_view(request):
    return HttpResponse("Public")

class PublicClassView(PublicViewMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Public view")

class SomeView(View):
    @method_decorator(public)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("Public view")

class DatatablesPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allow dynamic page size via query parameter

    def get_paginated_response(self, data):
        return Response({
            'recordsTotal': self.page.paginator.count,
            'recordsFiltered': self.page.paginator.count,
            'results': data
        })

class VlansViewSet(viewsets.ModelViewSet):
    queryset = Vlans.objects.all().order_by('id')
    serializer_class = VlansSerializer
    pagination_class = DatatablesPageNumberPagination
    filter_backends = (DatatablesFilterBackend,)

    def get_queryset(self):
        queryset = self.queryset
        search = self.request.query_params.get('search[value]', None)
        order_columns = self.request.query_params.getlist('order_columns[]')
        order_dirs = self.request.query_params.getlist('order_dirs[]')
        start = int(self.request.query_params.get('start', 0))
        length = int(self.request.query_params.get('length', 10))

        if search:
            queryset = queryset.filter(
                Q(vlan__icontains=search) |
                Q(i_sid__icontains=search) |
                Q(name__icontains=search) |
                Q(subnet__icontains=search) |
                Q(subnet_mask__icontains=search) |
                Q(default_gateway__icontains=search) |
                Q(vrrp_ip_address_1__icontains=search) |
                Q(vrrp_ip_address_2__icontains=search) |
                Q(vrf__icontains=search) |
                Q(dhcp__icontains=search) |
                Q(dhcp_server_1__icontains=search) |
                Q(dhcp_server_2__icontains=search) |
                Q(notes__icontains=search)
            )

        # Handle sorting
        order = []
        for column, direction in zip(order_columns, order_dirs):
            if direction == 'desc':
                column = f'-{column}'
            order.append(column)
        queryset = queryset.order_by(*order)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_records = self.queryset.count()
        filtered_records = queryset.count()
        start = int(request.query_params.get('start', 0))
        length = int(request.query_params.get('length', 10))
        page = queryset[start:start + length]
        serializer = self.get_serializer(page, many=True)
        return Response({
            'recordsTotal': total_records,
            'recordsFiltered': filtered_records,
            'results': serializer.data
        })

class CoreSubnetsViewSet(viewsets.ModelViewSet):
    queryset = CoreSubnets.objects.all().order_by('id')
    serializer_class = CoreSubnetsSerializer
    pagination_class = DatatablesPageNumberPagination
    filter_backends = (DatatablesFilterBackend,)

    def get_queryset(self):
        queryset = self.queryset
        search = self.request.query_params.get('search[value]', None)
        order_columns = self.request.query_params.getlist('order_columns[]')
        order_dirs = self.request.query_params.getlist('order_dirs[]')
        start = int(self.request.query_params.get('start', 0))
        length = int(self.request.query_params.get('length', 10))

        if search:
            queryset = queryset.filter(
                Q(core__icontains=search) |
                Q(subnets__icontains=search) |
                Q(vlan_name__icontains=search) |
                Q(vlan_id__icontains=search) |
                Q(guest_vrf_local__icontains=search) |
                Q(switch_port_pri__icontains=search) |
                Q(guest_vrf_sc__icontains=search) |
                Q(switch_port_sec__icontains=search) |
                Q(dhcp__icontains=search)
            )

        # Handle sorting
        order = []
        for column, direction in zip(order_columns, order_dirs):
            if direction == 'desc':
                column = f'-{column}'
            order.append(column)
        queryset = queryset.order_by(*order)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_records = self.queryset.count()
        filtered_records = queryset.count()
        start = int(request.query_params.get('start', 0))
        length = int(request.query_params.get('length', 10))
        page = queryset[start:start + length]
        serializer = self.get_serializer(page, many=True)
        return Response({
            'recordsTotal': total_records,
            'recordsFiltered': filtered_records,
            'results': serializer.data
        })

def vlans_data(request):
    viewset = VlansViewSet.as_view({'get': 'list'})
    return viewset(request)

def coresubnets_data(request):
    viewset = CoreSubnetsViewSet.as_view({'get': 'list'})
    return viewset(request)
