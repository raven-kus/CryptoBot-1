import logging
from services.abstract_service import *
from config.cst import *


class ServiceCreator:

    @classmethod
    def get_name(cls):
        return cls.__name__

    @staticmethod
    def create_services(config):
        logger = logging.getLogger(ServiceCreator.get_name())
        for service_class in AbstractService.__subclasses__():
            service_instance = service_class()
            if service_instance.get_is_enabled():
                service_instance.set_logger(logging.getLogger(service_class.get_name()))
                service_instance.set_config(config)
                if service_instance.has_required_configuration():
                    service_instance.prepare()
                    config[CONFIG_CATEGORY_SERVICES][service_instance.get_type()][CONFIG_SERVICE_INSTANCE] = service_instance
                else:
                    logger.error(service_class.get_name()+" can't be initialized: configuration is missing !")
