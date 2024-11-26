from pathlib import Path
from string import Template

SOLUTION_TEMPLATE_FILE = Path("templates", "solution.template.py")
TEST_TEMPLATE_FILE = Path("templates", "test.template.py")

with open(SOLUTION_TEMPLATE_FILE) as f:
    SOLUTION_TEMPLATE = f.read()

with open(TEST_TEMPLATE_FILE) as f:
    TEST_TEMPLATE = f.read()


def get_templates():
    return SOLUTION_TEMPLATE, Template(TEST_TEMPLATE)
