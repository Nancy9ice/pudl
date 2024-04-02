"""Definitions of data tables primarily coming from EIA-860."""

from typing import Any

RESOURCE_METADATA: dict[str, dict[str, Any]] = {
    "core_eia860__scd_boilers": {
        "description": (
            "Annually varying boiler attributes, compiled from across all EIA-860 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "boiler_id",
                "report_date",
                "boiler_operating_date",
                "boiler_status",
                "boiler_retirement_date",
                "boiler_type",
                "firing_type_1",
                "firing_type_2",
                "firing_type_3",
                "firing_rate_using_coal_tons_per_hour",
                "firing_rate_using_oil_bbls_per_hour",
                "firing_rate_using_gas_mcf_per_hour",
                "firing_rate_using_other_fuels",
                "boiler_fuel_code_1",
                "boiler_fuel_code_2",
                "boiler_fuel_code_3",
                "boiler_fuel_code_4",
                "waste_heat_input_mmbtu_per_hour",
                "wet_dry_bottom",
                "fly_ash_reinjection",
                "hrsg",
                "max_steam_flow_1000_lbs_per_hour",
                "turndown_ratio",
                "efficiency_100pct_load",
                "efficiency_50pct_load",
                "air_flow_100pct_load_cubic_feet_per_minute",
                "new_source_review",
                "new_source_review_date",
                "new_source_review_permit",
                "regulation_particulate",
                "regulation_so2",
                "regulation_nox",
                "standard_particulate_rate",
                "standard_so2_rate",
                "standard_nox_rate",
                "unit_particulate",
                "unit_so2",
                "unit_nox",
                "compliance_year_particulate",
                "compliance_year_nox",
                "compliance_year_so2",
                "particulate_control_out_of_compliance_strategy_1",
                "particulate_control_out_of_compliance_strategy_2",
                "particulate_control_out_of_compliance_strategy_3",
                "so2_control_out_of_compliance_strategy_1",
                "so2_control_out_of_compliance_strategy_2",
                "so2_control_out_of_compliance_strategy_3",
                "so2_control_existing_caaa_compliance_strategy_1",
                "so2_control_existing_caaa_compliance_strategy_2",
                "so2_control_existing_caaa_compliance_strategy_3",
                "so2_control_planned_caaa_compliance_strategy_1",
                "so2_control_planned_caaa_compliance_strategy_2",
                "so2_control_planned_caaa_compliance_strategy_3",
                "nox_control_out_of_compliance_strategy_1",
                "nox_control_out_of_compliance_strategy_2",
                "nox_control_out_of_compliance_strategy_3",
                "nox_control_existing_caaa_compliance_strategy_1",
                "nox_control_existing_caaa_compliance_strategy_2",
                "nox_control_existing_caaa_compliance_strategy_3",
                "nox_control_planned_caaa_compliance_strategy_1",
                "nox_control_planned_caaa_compliance_strategy_2",
                "nox_control_planned_caaa_compliance_strategy_3",
                "compliance_year_mercury",
                "mercury_control_existing_strategy_1",
                "mercury_control_existing_strategy_2",
                "mercury_control_existing_strategy_3",
                "mercury_control_existing_strategy_4",
                "mercury_control_existing_strategy_5",
                "mercury_control_existing_strategy_6",
                "mercury_control_proposed_strategy_1",
                "mercury_control_proposed_strategy_2",
                "mercury_control_proposed_strategy_3",
                "nox_control_existing_strategy_1",
                "nox_control_existing_strategy_2",
                "nox_control_existing_strategy_3",
                "nox_control_manufacturer",
                "nox_control_manufacturer_code",
                "nox_control_proposed_strategy_1",
                "nox_control_proposed_strategy_2",
                "nox_control_proposed_strategy_3",
                "nox_control_status_code",
                "regulation_mercury",
                "so2_control_existing_strategy_1",
                "so2_control_existing_strategy_2",
                "so2_control_existing_strategy_3",
                "so2_control_proposed_strategy_1",
                "so2_control_proposed_strategy_2",
                "so2_control_proposed_strategy_3",
                "standard_so2_percent_scrubbed",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "boiler_id", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "boiler_id", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with core_eia860__scd_generators, which is annual,
                # so non-january records violate the constraint.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "core_eia923__monthly_boiler_fuel",
                    "out_eia923__boiler_fuel",
                    "out_eia923__monthly_boiler_fuel",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "core_eia860__assn_boiler_generator": {
        "description": (
            "Associations between boilers and generators as reported in EIA-860 "
            "Schedule 6, Part A. Augmented with various heuristics within PUDL."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "generator_id",
                "boiler_id",
                "unit_id_eia",
                "unit_id_pudl",
                "boiler_generator_assn_type_code",
                "steam_plant_type_code",
                "bga_source",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "report_date", "generator_id", "boiler_id"],
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_generators": {
        "description": (
            "Annually varying generator attributes compiled from across EIA-860 and "
            "EIA-923 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "utility_id_eia",
                "report_date",
                "operational_status_code",
                "operational_status",
                "ownership_code",
                "capacity_mw",
                "summer_capacity_mw",
                "summer_capacity_estimate",
                "winter_capacity_mw",
                "winter_capacity_estimate",
                "net_capacity_mwdc",
                "energy_storage_capacity_mwh",
                "prime_mover_code",
                "energy_source_code_1",
                "energy_source_code_2",
                "energy_source_code_3",
                "energy_source_code_4",
                "energy_source_code_5",
                "energy_source_code_6",
                "energy_source_1_transport_1",
                "energy_source_1_transport_2",
                "energy_source_1_transport_3",
                "energy_source_2_transport_1",
                "energy_source_2_transport_2",
                "energy_source_2_transport_3",
                "fuel_type_code_pudl",
                "multiple_fuels",
                "deliver_power_transgrid",
                "distributed_generation",
                "syncronized_transmission_grid",
                "turbines_num",
                "planned_modifications",
                "planned_net_summer_capacity_uprate_mw",
                "planned_net_winter_capacity_uprate_mw",
                "planned_uprate_date",
                "planned_net_summer_capacity_derate_mw",
                "planned_net_winter_capacity_derate_mw",
                "planned_derate_date",
                "planned_new_prime_mover_code",
                "planned_energy_source_code_1",
                "planned_repower_date",
                "other_planned_modifications",
                "other_modifications_date",
                "planned_generator_retirement_date",
                "carbon_capture",
                "startup_source_code_1",
                "startup_source_code_2",
                "startup_source_code_3",
                "startup_source_code_4",
                "technology_description",
                "turbines_inverters_hydrokinetics",
                "time_cold_shutdown_full_load_code",
                "planned_new_capacity_mw",
                "cofire_fuels",
                "switch_oil_gas",
                "nameplate_power_factor",
                "minimum_load_mw",
                "uprate_derate_during_year",
                "uprate_derate_completed_date",
                "current_planned_generator_operating_date",
                "summer_estimated_capability_mw",
                "winter_estimated_capability_mw",
                "generator_retirement_date",
                "owned_by_non_utility",
                "reactive_power_output_mvar",
                "ferc_qualifying_facility",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "generator_id", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "generator_id", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with core_eia860__scd_generators, which is annual,
                # so non-january records violate the constraint.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "core_eia923__monthly_boiler_fuel",
                    "_out_eia__monthly_capacity_factor_by_generator",
                    "out_eia923__generation",
                    "out_eia923__monthly_generation",
                    "_out_eia__monthly_fuel_cost_by_generator",
                    "core_eia923__monthly_fuel_receipts_costs",
                    "core_eia923__monthly_generation",
                    "out_eia923__monthly_generation_fuel_by_generator_energy_source",
                    "out_eia923__monthly_generation_fuel_by_generator",
                    "core_eia923__monthly_generation_fuel",
                    "_out_eia__monthly_heat_rate_by_generator",
                    "_out_eia__monthly_derived_generator_attributes",
                    "out_eia__monthly_generators",
                    "core_eia860m__changelog_generators",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_ownership": {
        "description": (
            "Generator Ownership, reported in EIA-860 Schedule 4. Includes only "
            "jointly or third-party owned generators."
        ),
        "schema": {
            "fields": [
                "report_date",
                "owner_utility_id_eia",
                "plant_id_eia",
                "generator_id",
                "owner_utility_name_eia",
                "owner_state",
                "owner_city",
                "owner_country",
                "owner_street_address",
                "owner_zip_code",
                "fraction_owned",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "generator_id",
                "owner_utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "out_eia860__yearly_ownership": {
        "description": (
            "Generator Ownership, reported in EIA-860 Schedule 4. Includes only "
            "jointly or third-party owned generators. Denormalized to include plant "
            "and utility names and other associated IDs."
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "plant_id_pudl",
                "plant_name_eia",
                "owner_utility_id_eia",
                "utility_id_pudl",
                "owner_utility_name_eia",
                "generator_id",
                "owner_state",
                "owner_city",
                "owner_country",
                "owner_street_address",
                "owner_zip_code",
                "fraction_owned",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "generator_id",
                "owner_utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "outputs",
    },
    "core_eia860__scd_plants": {
        "description": (
            "Annually varying plant attributes, compiled from across all EIA-860 and "
            "EIA-923 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "ash_impoundment",
                "ash_impoundment_lined",
                "ash_impoundment_status",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
                "datum",
                "energy_storage",
                "ferc_cogen_docket_no",
                "ferc_cogen_status",
                "ferc_exempt_wholesale_generator_docket_no",
                "ferc_exempt_wholesale_generator",
                "ferc_small_power_producer_docket_no",
                "ferc_small_power_producer",
                "ferc_qualifying_facility_docket_no",
                "grid_voltage_1_kv",
                "grid_voltage_2_kv",
                "grid_voltage_3_kv",
                "iso_rto_code",
                "liquefied_natural_gas_storage",
                "natural_gas_local_distribution_company",
                "natural_gas_storage",
                "natural_gas_pipeline_name_1",
                "natural_gas_pipeline_name_2",
                "natural_gas_pipeline_name_3",
                "nerc_region",
                "net_metering",
                "pipeline_notes",
                "primary_purpose_id_naics",
                "regulatory_status_code",
                "reporting_frequency_code",
                "sector_id_eia",
                "sector_name_eia",
                "service_area",
                "transmission_distribution_owner_id",
                "transmission_distribution_owner_name",
                "transmission_distribution_owner_state",
                "utility_id_eia",
                "water_source",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with core_eia860__scd_plants, which is annual, so
                # non-january records fail.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "_core_eia923__cooling_system_information",
                    "_core_eia923__fgd_operation_maintenance",
                    "core_eia923__monthly_boiler_fuel",
                    "out_eia923__boiler_fuel",
                    "out_eia923__monthly_boiler_fuel",
                    "out_eia923__fuel_receipts_costs",
                    "out_eia923__monthly_fuel_receipts_costs",
                    "out_eia923__generation",
                    "out_eia923__monthly_generation",
                    "out_eia923__generation_fuel_combined",
                    "out_eia923__monthly_generation_fuel_combined",
                    "out_eia923__monthly_generation_fuel_by_generator_energy_source",
                    "out_eia923__monthly_generation_fuel_by_generator",
                    "core_eia923__monthly_fuel_receipts_costs",
                    "core_eia923__monthly_generation",
                    "core_eia923__monthly_generation_fuel",
                    "core_eia923__monthly_generation_fuel_nuclear",
                    "_out_eia__monthly_heat_rate_by_unit",
                    "_out_eia__monthly_heat_rate_by_generator",
                    "_out_eia__monthly_fuel_cost_by_generator",
                    "_out_eia__monthly_capacity_factor_by_generator",
                    "_out_eia__monthly_derived_generator_attributes",
                    "out_eia__monthly_generators",
                    "core_eia860m__changelog_generators",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_utilities": {
        "description": (
            "Annually varying utility attributes, compiled from all EIA data."
        ),
        "schema": {
            "fields": [
                "utility_id_eia",
                "report_date",
                "street_address",
                "city",
                "state",
                "zip_code",
                "plants_reported_owner",
                "plants_reported_operator",
                "plants_reported_asset_manager",
                "plants_reported_other_relationship",
                "entity_type",
                "attention_line",
                "address_2",
                "zip_code_4",
                "contact_firstname",
                "contact_lastname",
                "contact_title",
                "phone_number",
                "phone_extension",
                "contact_firstname_2",
                "contact_lastname_2",
                "contact_title_2",
                "phone_number_2",
                "phone_extension_2",
                "data_maturity",
            ],
            "primary_key": ["utility_id_eia", "report_date"],
            "foreign_key_rules": {
                "fields": [
                    ["utility_id_eia", "report_date"],
                    ["owner_utility_id_eia", "report_date"],
                ],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with core_eia860__scd_plants, which is annual, so
                # non-january records fail.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                # NOTE: EIA-861 has not gone through harvesting / normalization yet.
                "exclude": [
                    "core_eia861__yearly_advanced_metering_infrastructure",
                    "core_eia861__assn_balancing_authority",
                    "out_eia861__compiled_geometry_utilities",
                    "core_eia861__yearly_demand_response",
                    "core_eia861__yearly_demand_response_water_heater",
                    "core_eia861__yearly_demand_side_management_ee_dr",
                    "core_eia861__yearly_demand_side_management_misc",
                    "core_eia861__yearly_demand_side_management_sales",
                    "out_eia923__boiler_fuel",
                    "out_eia923__monthly_boiler_fuel",
                    "out_eia923__fuel_receipts_costs",
                    "out_eia923__monthly_fuel_receipts_costs",
                    "out_eia923__generation",
                    "out_eia923__monthly_generation",
                    "out_eia923__generation_fuel_combined",
                    "out_eia923__monthly_generation_fuel_combined",
                    "_out_eia__monthly_fuel_cost_by_generator",
                    "out_eia923__monthly_generation_fuel_by_generator_energy_source",
                    "out_eia923__monthly_generation_fuel_by_generator",
                    "core_eia860m__changelog_generators",
                    # Utility IDs in this table are owners, not operators, and we are
                    # not yet harvesting owner_utility_id_eia from core_eia860__scd_ownership.
                    # See https://github.com/catalyst-cooperative/pudl/issues/1393
                    "out_eia923__yearly_generation_fuel_by_generator_energy_source_owner",
                    "core_eia861__yearly_distributed_generation_fuel",
                    "core_eia861__yearly_distributed_generation_misc",
                    "core_eia861__yearly_distributed_generation_tech",
                    "core_eia861__yearly_distribution_systems",
                    "core_eia861__yearly_dynamic_pricing",
                    "core_eia861__yearly_energy_efficiency",
                    "out_ferc714__respondents_with_fips",
                    "core_eia861__yearly_green_pricing",
                    "_out_eia__monthly_derived_generator_attributes",
                    "out_eia__monthly_generators",
                    "core_eia861__yearly_mergers",
                    "core_eia861__yearly_net_metering_customer_fuel_class",
                    "core_eia861__yearly_net_metering_misc",
                    "core_eia861__yearly_non_net_metering_customer_fuel_class",
                    "core_eia861__yearly_non_net_metering_misc",
                    "core_eia861__yearly_operational_data_misc",
                    "core_eia861__yearly_operational_data_revenue",
                    "core_eia861__yearly_reliability",
                    "core_eia861__yearly_sales",
                    "core_eia861__yearly_service_territory",
                    "out_ferc714__summarized_demand",
                    "core_eia861__assn_utility",
                    "core_eia861__yearly_utility_data_misc",
                    "core_eia861__yearly_utility_data_nerc",
                    "core_eia861__yearly_utility_data_rto",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_emissions_control_equipment": {
        "description": (
            """The cost, type, operating status, retirement date, and install year of
emissions control equipment reported to EIA. Includes control ids for sulfur dioxide
(SO2), particulate matter, mercury, nitrogen oxide (NOX), and acid (HCl) gas
monitoring."""
        ),
        "schema": {
            "fields": [
                "report_year",
                "plant_id_eia",
                "emission_control_id_pudl",
                "data_maturity",
                "emission_control_equipment_type_code",
                "operational_status_code",
                "mercury_control_id_eia",
                "nox_control_id_eia",
                "particulate_control_id_eia",
                "so2_control_id_eia",
                "acid_gas_control",
                "emission_control_equipment_cost",
                "emission_control_operating_date",
                "emission_control_retirement_date",
            ],
            "primary_key": ["report_year", "plant_id_eia", "emission_control_id_pudl"],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "out_eia860__yearly_emissions_control_equipment": {
        "description": (
            """The cost, type, operating status, retirement date, and install year of
emissions control equipment reported to EIA. Includes control ids for sulfur dioxide
(SO2), particulate matter, mercury, nitrogen oxide (NOX), and acid (HCl) gas monitoring.
The denormalized version contains plant name, utility id, pudl id, and utility name
columns."""
        ),
        "schema": {
            "fields": [
                "report_year",
                "plant_id_eia",
                "plant_id_pudl",
                "plant_name_eia",
                "utility_id_eia",
                "utility_id_pudl",
                "utility_name_eia",
                "emission_control_id_pudl",
                "data_maturity",
                "emission_control_equipment_type_code",
                "operational_status_code",
                "operational_status",
                "mercury_control_id_eia",
                "nox_control_id_eia",
                "particulate_control_id_eia",
                "so2_control_id_eia",
                "acid_gas_control",
                "emission_control_equipment_cost",
                "emission_control_operating_date",
                "emission_control_retirement_date",
            ],
            "primary_key": ["report_year", "plant_id_eia", "emission_control_id_pudl"],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__assn_yearly_boiler_emissions_control_equipment": {
        "description": (
            """A table that links EIA boiler IDs to emissions control IDs for NOx, SO2,
mercury, and particulate monitoring. The relationship between the IDs is sometimes many
to many."""
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "emission_control_id_type",
                "emission_control_id_eia",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "emission_control_id_type",
                "emission_control_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__assn_boiler_cooling": {
        "description": "A table that links EIA boiler IDs to EIA cooling system IDs.",
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "cooling_id_eia",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "cooling_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__assn_boiler_stack_flue": {
        "description": (
            """A table that links EIA boiler IDs to EIA stack and/or flue
system IDs."""
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "stack_id_eia",
                "flue_id_eia",
                "stack_flue_id_eia",
                "stack_flue_id_pudl",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "stack_flue_id_pudl",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "_core_eia860__cooling_equipment": {
        "description": (
            "Information about cooling equipment at generation facilities, "
            "from EIA-860 Schedule 6D.\n\n"
            "Note: This table has been cleaned, but not harvested with other "
            "EIA 923 or 860 data. The same variables present in this table "
            "may show up in other _core tables in other years. Once this table "
            "has been harvested, it will be removed from the PUDL database."
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "plant_name_eia",
                "cooling_id_eia",
                "utility_id_eia",
                "utility_name_eia",
                "county",
                "state",
                "chlorine_equipment_cost",
                "chlorine_equipment_operating_date",
                "cooling_equipment_total_cost",
                "cooling_status_code",
                "cooling_system_operating_date",
                "cooling_type_1",
                "cooling_type_2",
                "cooling_type_3",
                "cooling_type_4",
                "cooling_water_discharge",
                "cooling_water_source",
                "intake_distance_shore_feet",
                "intake_distance_surface_feet",
                "intake_rate_100pct_gallons_per_minute",
                "outlet_distance_shore_feet",
                "outlet_distance_surface_feet",
                "percent_dry_cooling",
                "plant_summer_capacity_mw",
                "pond_cost",
                "pond_operating_date",
                "pond_surface_area_acres",
                "pond_volume_acre_feet",
                "power_requirement_mw",
                "steam_plant_type_code",
                "tower_cost",
                "tower_operating_date",
                "tower_type_1",
                "tower_type_2",
                "tower_type_3",
                "tower_type_4",
                "tower_water_rate_100pct_gallons_per_minute",
                "water_source_code",
                "water_source",
                "water_type_code",
            ],
            "primary_key": [
                "plant_id_eia",
                "utility_id_eia",
                "cooling_id_eia",
                "report_date",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "_core_eia860__fgd_equipment": {
        "description": (
            "Information about flue gas desulfurization equipment at generation facilities, "
            "from EIA-860 Schedule 6E. Note: This table has been cleaned, but not "
            "harvested with other EIA 923 or 860 data. The same variables present in "
            "this table may show up in other _core tables in other years. Once this "
            "table has been harvested, it will be removed from the PUDL database."
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "so2_control_id_eia",
                "utility_id_eia",
                "utility_name_eia",
                "state",
                "state_id_fips",
                "county",
                "county_id_fips",
                "fgd_operating_date",
                "fgd_operational_status_code",
                "flue_gas_bypass_fgd",
                "byproduct_recovery",
                "sludge_pond",
                "sludge_pond_lined",
                "pond_landfill_requirements_acre_foot_per_year",
                "fgd_structure_cost",
                "fgd_other_cost",
                "sludge_disposal_cost",
                "total_fgd_equipment_cost",
                "fgd_trains_100pct",
                "fgd_trains_total",
                "flue_gas_entering_fgd_pct_of_total",
                "flue_gas_exit_rate_cubic_feet_per_minute",
                "flue_gas_exit_temperature_fahrenheit",
                "so2_emission_rate_lbs_per_hour",
                "so2_equipment_type_1",
                "so2_equipment_type_2",
                "so2_equipment_type_3",
                "so2_equipment_type_4",
                "so2_removal_efficiency_design",
                "specifications_of_coal_ash",
                "specifications_of_coal_sulfur",
                "sorbent_type_1",
                "sorbent_type_2",
                "sorbent_type_3",
                "sorbent_type_4",
                "fgd_manufacturer",
                "fgd_manufacturer_code",
                "steam_plant_type_code",
                "plant_summer_capacity_mw",
                "water_source",
                "data_maturity",
            ],
            "primary_key": [
                "plant_id_eia",
                "so2_control_id_eia",
                "report_date",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_generators_wind": {
        "description": (
            "Annually reported information about wind generators from EIA-860 Schedule 3.2."
            " This table includes only those values that are unique to wind generators. "
            "The rest of the columns that are reported in the EIA-860 Wind tabs are "
            "included in core_eia860__scd_generators and core_eia__entity_generators."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "report_date",
                "design_wind_speed_mph",
                "obstacle_id_faa",
                "predominant_turbine_manufacturer",
                "predominant_turbine_model",
                "turbine_hub_height_feet",
                "wind_quality_class",
            ],
            "primary_key": [
                "plant_id_eia",
                "generator_id",
                "report_date",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_generators_solar": {
        "description": (
            "Annually reported information about solar generators from EIA-860 Schedule 3.3."
            " This table includes only those values that are unique to solar generators. "
            "The rest of the columns that are reported in the EIA-860 Solar tabs are "
            "included in core_eia860__scd_generators and core_eia__entity_generators."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "report_date",
                "standard_testing_conditions_capacity_mwdc",
                "net_metering_capacity_mwdc",
                "uses_net_metering_agreement",
                "uses_virtual_net_metering_agreement",
                "virtual_net_metering_capacity_mwdc",
                "azimuth_angle_deg",
                "tilt_angle_deg",
                "uses_technology_lenses_mirrors",
                "uses_technology_single_axis_tracking",
                "uses_technology_dual_axis_tracking",
                "uses_technology_fixed_tilt",
                "uses_technology_east_west_fixed_tilt",
                "uses_technology_parabolic_trough",
                "uses_technology_linear_fresnel",
                "uses_technology_power_tower",
                "uses_technology_dish_engine",
                "uses_technology_other",
                "uses_material_crystalline_silicon",
                "uses_material_thin_film_a_si",
                "uses_material_thin_film_cdte",
                "uses_material_thin_film_cigs",
                "uses_material_thin_film_other",
                "uses_material_other",
            ],
            "primary_key": [
                "plant_id_eia",
                "generator_id",
                "report_date",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "core_eia860__scd_generators_energy_storage": {
        "description": (
            "Annually reported information about energy storage from EIA-860 Schedule 3."
            " This table includes only those values that are unique to energy storage. "
            "The rest of the columns that are reported in the EIA-860 Energy Storage tabs are "
            "included in core_eia860__scd_generators and core_eia__entity_generators."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "report_date",
                "max_charge_rate_mw",
                "max_discharge_rate_mw",
                "storage_enclosure_code",
                "storage_technology_code_1",
                "storage_technology_code_2",
                "storage_technology_code_3",
                "storage_technology_code_4",
                "served_arbitrage",
                "served_backup_power",
                "served_co_located_renewable_firming",
                "served_frequency_regulation",
                "served_load_following",
                "served_load_management",
                "served_ramping_spinning_reserve",
                "served_system_peak_shaving",
                "served_transmission_and_distribution_deferral",
                "served_voltage_or_reactive_power_support",
                "stored_excess_wind_and_solar_generation",
            ],
            "primary_key": [
                "plant_id_eia",
                "generator_id",
                "report_date",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
}
"""EIA-860 resource attributes organized by PUDL identifier (``resource.name``).

Keys are in alphabetical order.

See :func:`pudl.metadata.helpers.build_foreign_keys` for the expected format of
``foreign_key_rules``.
"""
