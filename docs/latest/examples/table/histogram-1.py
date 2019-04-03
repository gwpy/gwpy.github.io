from gwpy.table import EventTable
events = EventTable.fetch_open_data(
    "GWTC-1-confident",
    columns=("mass1", "mass2"),
)
events.add_column(events["mass1"] + events["mass2"], name="mtotal")