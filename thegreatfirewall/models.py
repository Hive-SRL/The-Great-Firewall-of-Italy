from django.db import models

#Tabella che salva i ticket scaricati
class TicketPS(models.Model):
    ticket_id = models.CharField(max_length=200)
    dda_id = models.CharField(max_length=200)
    created_at = models.CharField(max_length=150)
    created_by = models.CharField(max_length=150)
    created_by_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    internal_status = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural= "TicketPS"

#Tabella che contiene gli FQDN bloccati, ogni entità è associato al ticket che ha comportato il blocco
class FqdnPS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    dns_status = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural= "FqdnPS"

#Tabella che contiene gli IPv4 bloccati, ogni entità è associato al ticket che ha comportato il blocco
class IPv4PS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    bgp_status = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural= "IPv4PS"

#Tabella che contiene gli IPv6 bloccati, ogni entità è associato al ticket che ha comportato il blocco
class IPv6PS(models.Model):
    ticket_id = models.ForeignKey(TicketPS, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    bgp_status = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural= "IPv6PS"

#Tabella che contiene le credenziali della piattaforma PiracyShield
class PiracyShieldAuth(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    access_token_expiration = models.IntegerField()
    refresh_token_expiration = models.IntegerField()
