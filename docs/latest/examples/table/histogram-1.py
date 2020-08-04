from gwpy.table import EventTable
events = EventTable.fetch_open_data(
    "GWTC-1-confident",
    columns=("mass_1_source", "mass_2_source"),
)
events.add_column(
    events["mass_1_source"] + events["mass_2_source"],
    name="mtotal"
)