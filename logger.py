import inspect
import logging
from contextlib import contextmanager

import allure


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log = logging.getLogger()


@contextmanager
def step(description: str) -> str:
    desc = description or _function_name()
    log.info('STEP %s', desc)
    with allure.step(desc) as s:
        yield s


def _function_name() -> str:
    return inspect.stack()[4][4][0].replace(' ', '').replace('\n', '')
