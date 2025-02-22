from django.db import models

class Vlans(models.Model):
    TRUE_FALSE_CHOICES = [
        (None, 'None'),
        (True, 'True'),
        (False, 'False'),
    ]
    vlan = models.IntegerField()
    i_sid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255, null=True, blank=True)
    subnet_mask = models.CharField(max_length=255, null=True, blank=True)
    default_gateway = models.CharField(max_length=255, null=True, blank=True)
    vrrp_ip_address_1 = models.CharField(max_length=255, null=True, blank=True)
    vrrp_ip_address_2 = models.CharField(max_length=255, null=True, blank=True)
    vrf = models.CharField(max_length=255, null=True, blank=True)
    dhcp = models.BooleanField(choices=TRUE_FALSE_CHOICES, null=True, blank=True, default=None)
    dhcp_server_1 = models.CharField(max_length=255, null=True, blank=True)
    dhcp_server_2 = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = '001_VLAN'
        verbose_name_plural = '001_VLANs'
        ordering = ['id']

    def __str__(self):
        return self.name if self.name else ''


class CoreSubnets(models.Model):
    core = models.CharField(max_length=255)
    subnets = models.CharField(max_length=255)
    vlan_name = models.CharField(max_length=255)
    vlan_id = models.IntegerField()
    guest_vrf_local = models.CharField(max_length=255, null=True, blank=True)
    switch_port_pri = models.CharField(max_length=255, null=True, blank=True)
    guest_vrf_sc = models.CharField(max_length=255, null=True, blank=True)
    switch_port_sec = models.CharField(max_length=255, null=True, blank=True)
    dhcp = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = '002_CoreSubnets'
        verbose_name_plural = '002_CoreSubnets'
        ordering = ['id']

    def __str__(self):
        return self.vlan_name if self.vlan_name else ''
