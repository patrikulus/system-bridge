"""System Bridge Connector: Constants"""

# Settings
SETTING_LOG_LEVEL = "log_level"
SETTING_PORT_API = "port_api"

# Secrets
SECRET_API_KEY = "api_key"

# Event Keys
EVENT_DATA = "data"
EVENT_EVENT = "event"
EVENT_ID = "id"
EVENT_MESSAGE = "message"
EVENT_MODULE = "module"
EVENT_MODULES = "modules"
EVENT_SETTING = "setting"
EVENT_SUBTYPE = "subtype"
EVENT_TYPE = "type"
EVENT_VALUE = "value"

# Event Types
SUBTYPE_BAD_API_KEY = "BAD_API_KEY"
SUBTYPE_BAD_JSON = "BAD_JSON"
SUBTYPE_LISTENER_ALREADY_REGISTERED = "LISTENER_ALREADY_REGISTERED"
SUBTYPE_LISTENER_NOT_REGISTERED = "LISTENER_NOT_REGISTERED"
SUBTYPE_MISSING_API_KEY = "MISSING_API_KEY"
SUBTYPE_MISSING_KEY = "MISSING_KEY"
SUBTYPE_MISSING_MODULES = "MISSING_MODULES"
SUBTYPE_MISSING_PATH_URL = "MISSING_PATH_URL"
SUBTYPE_MISSING_SETTING = "MISSING_SETTING"
SUBTYPE_MISSING_TEXT = "MISSING_TEXT"
SUBTYPE_MISSING_VALUE = "MISSING_VALUE"
SUBTYPE_UNKNOWN_EVENT = "UNKNOWN_EVENT"
TYPE_DATA_GET = "DATA_GET"
TYPE_DATA_LISTENER_REGISTERED = "DATA_LISTENER_REGISTERED"
TYPE_DATA_LISTENER_UNREGISTERED = "DATA_LISTENER_UNREGISTERED"
TYPE_DATA_UPDATE = "DATA_UPDATE"
TYPE_ERROR = "ERROR"
TYPE_EXIT_APPLICATION = "EXIT_APPLICATION"
TYPE_GET_DATA = "GET_DATA"
TYPE_GET_SETTING = "GET_SETTING"
TYPE_GET_SETTINGS = "GET_SETTINGS"
TYPE_KEYBOARD_KEY_PRESSED = "KEYBOARD_KEY_PRESSED"
TYPE_KEYBOARD_KEYPRESS = "KEYBOARD_KEYPRESS"
TYPE_KEYBOARD_TEXT = "KEYBOARD_TEXT"
TYPE_KEYBOARD_TEXT_SENT = "KEYBOARD_TEXT_SENT"
TYPE_OPEN = "OPEN"
TYPE_OPENED = "OPENED"
TYPE_REGISTER_DATA_LISTENER = "REGISTER_DATA_LISTENER"
TYPE_SETTING_RESULT = "SETTING_RESULT"
TYPE_SETTING_UPDATED = "SETTING_UPDATED"
TYPE_SETTINGS_RESULT = "SETTINGS_RESULT"
TYPE_UNREGISTER_DATA_LISTENER = "UNREGISTER_DATA_LISTENER"
TYPE_UPDATE_SETTING = "UPDATE_SETTING"