from homeassistant.config_entries import ConfigFlow
from .const import DOMAIN

class LwlcomtvConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""

    async def async_step_user(self, formdata):
        return self.async_create_entry(title="LWLcom TV")
