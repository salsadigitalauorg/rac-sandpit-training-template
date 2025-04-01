FROM ghcr.io/salsadigitalauorg/salsa-images/rules-as-code:latest

# Remove the default existing rules
RUN rm -rf /app/openfisca-rules/openfisca_rules/*
# Copy the new project rules
COPY openfisca_rules /app/openfisca-rules/openfisca_rules
