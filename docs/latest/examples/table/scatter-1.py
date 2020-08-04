from gwpy.table import EventTable
events = EventTable.fetch_open_data(
    "GWTC-1-confident",
    columns=(
        "mass_1_source",
        "mass_2_source",
        "chirp_mass_source",
        "luminosity_distance"
    ),
)