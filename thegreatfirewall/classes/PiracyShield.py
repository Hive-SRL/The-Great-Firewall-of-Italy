import requests
import json
from django.conf import settings


class PiracyShield:
    def __init__(self):
        self.url = settings.PIRACY_URL
        pass

    #Gestione credenziali
    def login(self, access_token, email, password):
        try:
            url = self.url + '/api/v1/authentication/login'
            payload = json.dumps({
                'email': email,
                'password': password
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)

    def renew_refresh_token(self, access_token, refresh_token):
        try:
            url = self.url + '/api/v1/authentication/refresh'
            payload = json.dumps({
                'refresh_token': refresh_token
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)

    def logout(self, access_token):
        try:
            url = self.url + '/api/v1/authentication/logout'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

#SEZIONE TICKET
    def getSingleTicket(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)
    def getTickets(self, access_token):
        try:
            url = self.url + '/api/v1/ticket/get/all'

            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def setTicketItemProcessed(self, access_token, ticket_item_value):
        try:
            url = self.url + '/api/v1/ticket/item/set/processed '
            payload = json.dumps({
                'ticket_item_value': ticket_item_value
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)
    def setTicketItemUnprocessed(self, access_token, ticket_item_value, reason):
        try:
            url = self.url + '/api/v1/ticket/item/set/unprocessed '
            payload = json.dumps({
                'ticket_item_value': ticket_item_value,
                'reason': reason
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)

    #SEZIONE FQDN
    def getAllFqdn(self, access_token):
        try:
            url = self.url + '/api/v1/fqdn/get/all'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getAllTXTFqdn(self, access_token):
        try:
            url = self.url + '/api/v1/fqdn/get/all/txt'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)
    def getAllChecksumFqdn(self, access_token):
        try:
            url = self.url + '/api/v1/fqdn/get/all/checksum'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getFqdnByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/fqdn'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getFqdnTXTByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/fqdn/txt'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getFqdnChecksumByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/fqdn/txt/checksum'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    #SEZIONE IPv4
    def getIPv4All(self, access_token):
        try:
            url = self.url + '/api/v1/ipv4/get/all'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)
    def getIPv4TXTAll(self, access_token):
        try:
            url = self.url + '/api/v1/ipv4/get/all/txt'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv4ChecksumAll(self, access_token):
        try:
            url = self.url + '/api/v1/ipv4/get/all/checksum'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)
    def getIPv4ByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv4'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv4TXTByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv4/txt'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv4ChecksumByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv4/txt/checksum'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)


    #Sezione IPv6

    def getIPv6All(self, access_token):
        try:
            url = self.url + '/api/v1/ipv6/get/all'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv6TXTAll(self, access_token):
        try:
            url = self.url + '/api/v1/ipv6/get/all/txt'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv6ChecksumAll(self, access_token):
        try:
            url = self.url + '/api/v1/ipv6/get/all/checksum'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)
    def getIPv6ByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv6'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv6TXTByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv6/txt'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    def getIPv6ChecksumByTicketId(self, access_token, ticket_id):
        try:
            url = self.url + '/api/v1/ticket/get/ipv6/txt/checksum'
            payload = json.dumps({
                'ticket_id': ticket_id
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    #SEZIONE WHITELIST
    #Attenzione in documentazione è una GET, forse un errore
    def insertWhitelistItem(self, access_token, genre, item, registrar):
        try:
            url = self.url + '/api/v1/whitelist/item/create'
            payload = json.dumps({
                'genre': genre,
                'item': item,
                'registrar': registrar
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)

    def getAllWhitelistItems(self, access_token):
        try:
            url = self.url + '/api/v1/whitelist/item/get/all'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            # TODO implementare logging
            return response.text
        except requests.exceptions as e:
            # TODO implementare logging
            print(e)

    # Attenzione! UNA DELETE CON UNA GET, forse un errore
    def removeWhitelistItem(self, access_token, genre, item):
        try:
            url = self.url + '/api/v1/whitelist/item/remove'
            payload = json.dumps({
                'genre': genre,
                'item': item
            })
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            return response.text
        except requests.exceptions as e:
            print(e)

    #ALTRO
    def ping(self, access_token):
        try:
            url = self.url + '/api/v1/ping'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.request("GET", url, headers=headers)
            return response.text
        except requests.exceptions as e:
            print(e)