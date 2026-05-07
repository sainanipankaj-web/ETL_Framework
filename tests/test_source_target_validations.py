import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from validations.source_target_validations import (
    validate_source_target_count,
    validate_salary_match
)

# =========================
# SOURCE TARGET COUNT VALIDATION
# =========================

def test_source_target_count():

    validate_source_target_count()


# =========================
# SALARY MATCH VALIDATION
# =========================

def test_salary_match():

    validate_salary_match()