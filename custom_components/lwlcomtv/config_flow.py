from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from aiohttp import ClientError, ClientResponseError, ClientSession
from .const import DOMAIN

class LwlcomtvConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""

    async def async_step_user(self, formdata):
        websession = async_get_clientsession(self.hass)

        try:
            async with websession.get('https://api.iptv.lwlcom.net/v1/channels') as response:
                response.raise_for_status()
                response_json = await response.json()
                channels = []
                for item in response_json:
                    if item['unicastStream'] != '':
                        channels.append({
                            'title': item['name'],
                            'logo': item['logo'],
                            'video': item['unicastStream']
                        })
                return self.async_create_entry(title="LWLcom TV",data={'channels': channels})
        except ClientError as exc:
            return self.async_abort(reason="channel_load")
