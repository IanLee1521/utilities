import logging
import logging.config


def configure_logging(verbose=False):
    DEFAULT_LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(message)s"
            },
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "standard",
                "class": "logging.StreamHandler",
            },
            "null": {
                "level": "INFO",
                "formatter": "standard",
                "class": "logging.NullHandler",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": "DEBUG", "propagate": False},
        },
    }

    if verbose:
        DEFAULT_LOGGING["handlers"]["default"]["level"] = "DEBUG"

    logging.config.dictConfig(DEFAULT_LOGGING)
