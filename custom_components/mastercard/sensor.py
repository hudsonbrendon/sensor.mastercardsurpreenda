import logging
from datetime import timedelta

import homeassistant.helpers.config_validation as cv
import requests
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.entity import Entity
from homeassistant.util.dt import utc_from_timestamp

_LOGGER = logging.getLogger(__name__)

ICON = "mdi:cash"

SCAN_INTERVAL = timedelta(minutes=60)

ATTRIBUTION = "Data provided by mastercard surpreenda"

DOMAIN = "mastercard"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_EMAIL): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
    }
)


def _request(email: str, password: str) -> dict:
    """Request data from mastercard."""
    url = "https://surpreenda.naotempreco.com.br/surpreenda/rest/v2/mrs/signIn"
    json = {"login": email, "password": password}
    response = requests.post(url, json=json)
    return response.json()

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the currency sensor"""

    email = config["email"]
    password = config["password"]

    add_entities(
        [MasterCardSensor(hass, email, password, SCAN_INTERVAL)],
        True,
    )


class MasterCardSensor(Entity):
    def __init__(self, hass, email, passowrd, interval):
        """Inizialize sensor"""
        self._hass = hass
        self._interval = interval
        self._email = email
        self._password = passowrd
        self._name = "Mastercard Surpreenda Pontuação"
        self._state = STATE_UNKNOWN
        self._last_updated = STATE_UNKNOWN

    @property
    def name(self):
        """Return the name sensor"""
        return self._name

    @property
    def icon(self):
        """Return the default icon"""
        return ICON

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._punctuation

    @property
    def last_updated(self):
        """Returns date when it was last updated."""
        if self._last_updated != 'unknown':
            stamp = float(self._last_updated)
            return utc_from_timestamp(int(stamp))

    @property
    def device_state_attributes(self):
        """Attributes."""
        return {"pontuacao": self._punctuation}

    def update(self):
        """Get the latest update fron the api"""
        response = _request(self._email, self._password)
        self._punctuation = response["balance"]
