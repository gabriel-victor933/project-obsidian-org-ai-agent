import logging
from datetime import datetime
import random

from litellm.integrations.custom_logger import CustomLogger


class AgentCustomLogger(CustomLogger):

    def __init__(self, name: str = 'default'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        timestamp = int(datetime.utcnow().timestamp())
        rand_diff = random.randint(1, 1000)
        log_file_name = f"logs/agent-{timestamp}-{rand_diff}.txt"

        handler = logging.FileHandler(log_file_name)

        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        self.logger.addHandler(handler)

        self.logger.propagate = False 

    def log_pre_api_call(self, model, messages, kwargs):
        self.logger.info(f"Pre-API Call: model={model}")

    def log_post_api_call(self, kwargs, response_obj, start_time, end_time):
        self.logger.info(f"Post-API Call: model={kwargs.get('model')}")

    def log_success_event(self, kwargs, response_obj, start_time, end_time):
        usage = getattr(response_obj, "usage", None)
        model = kwargs.get("model")
        self.logger.info(f"Success: model={model} | usage={usage} | duração={end_time - start_time}")

    def log_failure_event(self, kwargs, response_obj, start_time, end_time):
        exception = kwargs.get("exception")
        self.logger.error(f"Failure: model={kwargs.get('model')} | erro={exception}")