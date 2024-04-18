import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import logging

_LOGGER = logging.getLogger(__name__)

class Smart2000ESPConfigFlow(config_entries.ConfigFlow, domain="smart2000esp"):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        _LOGGER.debug("async_step_user called with user_input: %s", user_input)
        errors = {}
        
        if user_input is not None:
            existing_names = {entry.data.get("name") for entry in self._async_current_entries()}
            _LOGGER.debug("Existing names in the integration: %s", existing_names)
            
            if user_input["name"] in existing_names:
                _LOGGER.debug("Name exists error")
                errors["name"] = "name_exists"
            else:
                _LOGGER.debug("User input is valid, creating entry with name: %s", user_input.get('name'))
                return self.async_create_entry(title=user_input.get('name'), data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("name"): str,
                vol.Optional("pgn_include"): str,
                vol.Optional("pgn_exclude"): str,
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        _LOGGER.debug("Getting options flow handler")
        return OptionsFlowHandler(config_entry)



class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        _LOGGER.debug("Initializing OptionsFlowHandler with config_entry: %s", config_entry)
        self.config_entry = config_entry
        # Log the initial state of the config entry for debugging
        _LOGGER.debug("Initial config_entry data: %s", self.config_entry.data)

    async def async_step_init(self, user_input=None):
        _LOGGER.debug("OptionsFlowHandler.async_step_init called with user_input: %s", user_input)
    
        # Log the current options before any updates
        current_data = self.config_entry.data
        _LOGGER.debug("Current options before any updates: %s", current_data)
    
        if user_input is not None:
            _LOGGER.debug("Processing user input")
    
            _LOGGER.debug("Received user_input: %s", user_input)
    
            new_data = {**self.config_entry.data, **user_input}
            _LOGGER.debug("New data after processing user_input: %s", new_data)
    
            # Update the config entry with new data.
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                data=new_data
            )
            
            _LOGGER.debug("data updated with user input. New data: %s", new_data)
    
            return self.async_create_entry(title="", data=None)
        
        else:
            # No user input received, initialize options flow form with defaults.
            defaults = {
                "pgn_include": "   " + current_data.get("pgn_include", "").lstrip(),
                "pgn_exclude": "   " + current_data.get("pgn_exclude", "").lstrip(),
            }

            _LOGGER.debug("Form defaults: %s", defaults)

            return self.async_show_form(
                step_id="init",
                data_schema=vol.Schema({
                    vol.Optional("pgn_include", default=defaults["pgn_include"]): str,
                    vol.Optional("pgn_exclude", default=defaults["pgn_exclude"]): str,
                }),
            )