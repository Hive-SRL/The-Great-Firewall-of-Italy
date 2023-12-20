from django.db import models


class TicketPS(models.Model):
    ticket_id = models.CharField(max_length=200)
    dda_id = models.CharField(max_length=200)
    created_at = models.CharField(max_length=150)
    created_by = models.CharField(max_length=150)
    created_by_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    internal_status = models.CharField(max_length=100)


class FqdnPS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    url = models.CharField(100)
    status = models.CharField(100)
    dns_status = models.CharField(50)


class IPv4PS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    bgp_status = models.CharField(max_length=50)


class IPv6PS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    bgp_status = models.CharField(max_length=50)
