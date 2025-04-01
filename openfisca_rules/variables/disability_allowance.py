"""This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *

# Import the Entities specifically defined for this tax and benefit system
from openfisca_rules.entities import Person


# This variable is a pure input: it doesn't have a formula
class has_disability(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "I <do/do not> have a disability"
    reference = "https://law.gov.example/has_disability"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class monthly_income(Variable):
    value_type = float
    entity = Person
    definition_period = DAY
    label = "What is your monthly income"
    reference = "https://law.gov.example/monthly_income"  # Always use the most official source
    documentation = "Monthly income refers to your monthly taxable income"


# This variable has a formula that runs calculations
class disability_allowance_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Disability allowance eligibility"
    reference = "https://law.gov.example/disability_allowance_eligible"  # Always use the most official source

    def formula(person, period, parameters):
        """Calculate Disability Allowance eligibility."""
        # Retrieve the values of the input variables
        has_disability = person("has_disability", period)
        monthly_income = person("monthly_income", period)

        # Retrieve the parameter value for the maximum income
        disability_allowance_max_income = parameters(period).disability_allowance_max_income
        # Monthly income condition
        meets_the_income_criteria = monthly_income < disability_allowance_max_income

        # Return the result of the eligibility calculation
        return has_disability * meets_the_income_criteria
