"""Tables definitions for data coming from the FERC Form 714."""

from typing import Any

RESOURCE_METADATA: dict[str, dict[str, Any]] = {
    "core_ferc714__respondent_id": {
        "description": "Respondent identification. FERC Form 714, Part I, Schedule 1.",
        "schema": {
            "fields": [
                "respondent_id_ferc714",
                "respondent_name_ferc714",
                "eia_code",
            ],
            "primary_key": ["respondent_id_ferc714"],
            "foreign_key_rules": {"fields": [["respondent_id_ferc714"]]},
        },
        "sources": ["ferc714"],
        "field_namespace": "ferc714",
        "etl_group": "ferc714",
    },
    "out_ferc714__hourly_planning_area_demand": {
        "description": (
            "Hourly electricity demand by planning area. FERC Form 714, Part III, "
            "Schedule 2a."
        ),
        "schema": {
            "fields": [
                "respondent_id_ferc714",
                "report_date",
                "datetime_utc",
                "timezone",
                "demand_mwh",
            ],
            "primary_key": ["respondent_id_ferc714", "datetime_utc"],
        },
        "sources": ["ferc714"],
        "field_namespace": "ferc714",
        "etl_group": "ferc714",
        "create_database_schema": False,
    },
    "out_ferc714__respondents_with_fips": {
        "description": (
            "Annual respondents with the county FIPS IDs for their service territories."
        ),
        "schema": {
            "fields": [
                "eia_code",
                "respondent_type",
                "respondent_id_ferc714",
                "respondent_name_ferc714",
                "report_date",
                "balancing_authority_id_eia",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
                "utility_id_eia",
                "utility_name_eia",
                "state",
                "county",
                "state_id_fips",
                "county_id_fips",
            ]
            # No primary key here because the state and county FIPS columns
            # which are part of the natural primary key can be null.
            # The natural primary key would be:
            # ['respondent_id_ferc714', 'report_date', 'state_id_fips', 'county_id_fips']
        },
        "sources": ["ferc714"],
        "field_namespace": "ferc714",
        "etl_group": "outputs",
    },
    "out_ferc714__summarized_demand": {
        "description": (
            "Compile FERC 714 annualized, categorized respondents and summarize values."
        ),
        "schema": {
            "fields": [
                "report_date",
                "respondent_id_ferc714",
                "demand_annual_mwh",
                "population",
                "area_km2",
                "population_density_km2",
                "demand_annual_per_capita_mwh",
                "demand_density_mwh_km2",
                "eia_code",
                "respondent_type",
                "respondent_name_ferc714",
                "balancing_authority_id_eia",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
                "utility_id_eia",
                "utility_name_eia",
            ],
            "primary_key": ["respondent_id_ferc714", "report_date"],
        },
        "sources": ["ferc714"],
        "field_namespace": "ferc714",
        "etl_group": "outputs",
    },
    "core_ferc714__yearly_planning_area_demand_forecast": {
        "description": (
            "10-year forecasted summer and winter peak demand and annual net energy per planning area. FERC Form 714, Part III, "
            "Schedule 2b."
        ),
        "schema": {
            "fields": [
                "respondent_id_ferc714",
                "report_year",
                "forecast_year",
                "summer_peak_demand_mw",
                "winter_peak_demand_mw",
                "net_demand_mwh",
            ],
            "primary_key": ["respondent_id_ferc714", "report_year", "forecast_year"],
        },
        "sources": ["ferc714"],
        "field_namespace": "ferc714",
        "etl_group": "ferc714",
        "create_database_schema": True,
    },
}
"""FERC Form 714 resource attributes by PUDL identifier (``resource.name``).

Keys are in alphabetical order.

See :func:`pudl.metadata.helpers.build_foreign_keys` for the expected format of
``foreign_key_rules``.
"""
