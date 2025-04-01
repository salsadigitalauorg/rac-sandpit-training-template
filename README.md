## OpenFisca app template

This project aims to provide a scaffolding template of the OpenFisca country template for OpenFisca Web API applications.

### Dependencies
- VSCode: https://code.visualstudio.com/download
- Docker Desktop: https://www.docker.com/products/docker-desktop/

### Clone and Build
Clone this repo as a starting point.

#### Use the VSCode Dev Container

`Dev Containers: Open Folder in Container`

## Steps to Encode Rules with TDD

### Why Use Test-Driven Development (TDD)
- Accuracy: Ensures that our implementation exactly matches the specified requirements.
- Maintainability: Allows for easy updates to the system without breaking existing features.
- Documentation: Acts as both a guide and a specification for how the system should work.
- Quality Assurance: Helps in catching bugs early, increasing the reliability and stability of the application.

### Project Structure
- ./openfisca_rules/tests: Includes all TDD test cases that guide development and ensure functionality.
- ./openfisca_rules/parameters: Holds YAML files that specify various parameters like thresholds and rates that can change over time.
- ./openfisca_rules/entities.py: Defines the entities such as individuals, families, etc.
- ./openfisca_rules/variables: Contains the definitions of each variable, such as tax rates, salaries, etc.

### Encoding rules
1. Create YAML Tests: Begin by writing YAML tests that define the expected behaviour and outcomes of the simulation. These tests are crucial for verifying that your implementation meets the specified requirements.
2. Create Parameters: Define parameters such as tax rates, thresholds, minimum age/wage, and social security contributions. These values are essential inputs that influence the system's calculations.
3. Create Entities: Entities are the fundamental objects in OpenFisca, such as households, individuals, and companies. Define the entities relevant to your domain.
5. Create Input Variables: Input variables are an entity's property values, such as a person's income, age, or number of children. They are used to compute the output variables.
6. Create Output Variables and Formulas: Define the output variables that the system will calculate, such as tax owed, benefits received, or eligibility. The formulas for these output variables dictate how they are computed from the input variables and parameters.
7. Execute Tests: Run the YAML tests you created to ensure the model behaves as expected. This step helps catch any errors or discrepancies in the model.
