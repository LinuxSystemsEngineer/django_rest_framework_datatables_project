from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from .models import Vlans, CoreSubnets

class VlansAdmin(admin.ModelAdmin):
    list_display = ('id', 'vlan', 'i_sid', 'name', 'subnet', 'subnet_mask', 'default_gateway', 'vrrp_ip_address_1', 'vrrp_ip_address_2', 'vrf', 'dhcp', 'dhcp_server_1', 'dhcp_server_2', 'notes')
    search_fields = ('vlan', 'i_sid', 'name', 'subnet', 'subnet_mask', 'default_gateway', 'vrrp_ip_address_1', 'vrrp_ip_address_2', 'vrf', 'dhcp', 'dhcp_server_1', 'dhcp_server_2', 'notes')
    actions = ['edit_selected']
    list_per_page = 10

    def edit_selected(self, request, queryset):
        if queryset.count() == 1:
            obj = queryset.first()
            return redirect(reverse('admin:vlans_vlans_change', args=[obj.pk]))
    edit_selected.short_description = "Edit selected VLANs"

class CoreSubnetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'core', 'subnets', 'vlan_name', 'vlan_id', 'guest_vrf_local', 'switch_port_pri', 'guest_vrf_sc', 'switch_port_sec', 'dhcp')
    search_fields = ('core', 'subnets', 'vlan_name', 'vlan_id', 'guest_vrf_local', 'switch_port_pri', 'guest_vrf_sc', 'switch_port_sec', 'dhcp')
    list_per_page = 10

admin.site.register(Vlans, VlansAdmin)
admin.site.register(CoreSubnets, CoreSubnetsAdmin)
