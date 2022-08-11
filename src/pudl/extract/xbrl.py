"""Generic extractor for all FERC XBRL data."""
import io
import json
import time
from datetime import datetime

import sqlalchemy as sa
from ferc_xbrl_extractor import xbrl
from ferc_xbrl_extractor.instance import InstanceBuilder

import pudl
from pudl.helpers import get_logger
from pudl.settings import FercToSqliteSettings
from pudl.workspace.datastore import Datastore

logger = get_logger(__name__)

TAXONOMY_MAP = {
    1: "https://eCollection.ferc.gov/taxonomy/form1/2022-01-01/form/form1/form-1_2022-01-01.xsd",
    2: "https://eCollection.ferc.gov/taxonomy/form2/2022-01-01/form/form2/form-2_2022-01-01.xsd",
    6: "https://eCollection.ferc.gov/taxonomy/form6/2022-01-01/form/form6/form-6_2022-01-01.xsd",
    60: "https://eCollection.ferc.gov/taxonomy/form60/2022-01-01/form/form60/form-60_2022-01-01.xsd",
    714: "https://eCollection.ferc.gov/taxonomy/form714/2022-01-01/form/form714/form-714_2022-01-01.xsd",
}
"""Map FERC form number to the most recently published taxonomy URL."""


class FercXbrlDatastore:
    """Simple datastore wrapper for accessing ferc1 xbrl resources."""

    def __init__(self, datastore: Datastore):
        """Instantiate datastore wrapper for ferc1 resources."""
        self.datastore = datastore

    def get_filings(self, year: int, form_number: int):
        """Return list of filings from archive."""
        archive = self.datastore.get_zipfile_resource(f"ferc{form_number}", year=year)

        # Load RSS feed metadata
        filings = []
        with archive.open("rssfeed") as f:
            metadata = json.load(f)

            # Loop through all filings by a given filer in a given quarter
            # And take the most recent one
            for key, filing_info in metadata.items():
                latest = datetime.min
                for filing_id, info in filing_info.items():
                    # Parse date from 9-tuple
                    published = datetime.fromtimestamp(
                        time.mktime(tuple(info["published_parsed"]))
                    )

                    if published > latest:
                        latest_filing = f"{filing_id}.xbrl"

                # Create in memory buffers with file data to be used in conversion
                filings.append(
                    InstanceBuilder(
                        io.BytesIO(archive.open(latest_filing).read()), filing_id
                    )
                )

        return filings


def _get_sqlite_engine(
    form_number: int, pudl_settings: dict, clobber: bool
) -> sa.engine.Engine:
    """Create SQLite engine for specified form and drop tables.

    Args:
        form_number: FERC form number.
        pudl_settings: Dictionary of settings.
        clobber: Flag indicating whether or not to drop tables.
    """
    # Read in the structure of the DB, if it exists
    logger.info(f"Dropping the old FERC Form {form_number} SQLite DB if it exists.")
    sqlite_engine = sa.create_engine(pudl_settings[f"ferc{form_number}_xbrl_db"])
    try:
        # So that we can wipe it out
        pudl.helpers.drop_tables(sqlite_engine, clobber=clobber)
    except sa.exc.OperationalError:
        pass

    return sqlite_engine


def xbrl2sqlite(
    ferc_to_sqlite_settings: FercToSqliteSettings = FercToSqliteSettings(),
    pudl_settings: dict = None,
    clobber: bool = False,
    datastore: Datastore = None,
    batch_size: int | None = None,
    workers: int | None = None,
):
    """Clone the FERC Form 1 XBRL Databsae to SQLite.

    Args:
        ferc_to_sqlite_settings: Object containing Ferc to SQLite validated
            settings.
        pudl_settings: Dictionary containing paths and database URLs
            used by PUDL.
        datastore: Instance of a datastore to access the resources.
        batch_size: Number of XBRL filings to process in a single CPU process.
        workers: Number of CPU processes to create for processing XBRL filings.

    Returns:
        None

    """
    datastore = FercXbrlDatastore(datastore)

    # Handle Form 1 explicitly
    sqlite_engine = _get_sqlite_engine(1, pudl_settings, clobber)
    convert_form(
        1,
        ferc_to_sqlite_settings.ferc1_xbrl_to_sqlite_settings.years,
        datastore,
        sqlite_engine,
        taxonomy=ferc_to_sqlite_settings.ferc1_xbrl_to_sqlite_settings.taxonomy,
        batch_size=batch_size,
        workers=workers,
    )

    # Loop through all other forms and perform conversion
    for form in ferc_to_sqlite_settings.ferc_other_xbrl_to_sqlite_settings.forms:
        sqlite_engine = _get_sqlite_engine(form, pudl_settings, clobber)
        convert_form(
            form,
            ferc_to_sqlite_settings.ferc_other_xbrl_to_sqlite_settings.years,
            datastore,
            sqlite_engine,
            batch_size=batch_size,
            workers=workers,
        )


def convert_form(
    form_number: int,
    years: list[int],
    datastore: FercXbrlDatastore,
    sqlite_engine: sa.engine.Engine,
    batch_size: int | None = None,
    workers: int | None = None,
    taxonomy: str | None = None,
):
    """Clone a single FERC XBRL form to SQLite.

    Args:
        form_number: FERC form number (can be 1, 2, 6, 60, 714).
        years: List of validated years to process.
        datastore: Instance FERC XBRL datastore for retrieving data.
        sqlite_engine: SQLAlchemy connection to mirrored database.
        batch_size: Number of XBRL filings to process in a single CPU process.
        workers: Number of CPU processes to create for processing XBRL filings.
        taxonomy: URL of XBRL taxonomy to use for interpreting structure of XBRL filings.
            will override form_number if present

    Returns:
        None

    """
    # Handle FERC 1
    for year in years:
        xbrl.extract(
            datastore.get_filings(year, 1),
            sqlite_engine,
            batch_size=batch_size,
            workers=workers,
        )
