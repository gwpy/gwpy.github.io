from gwpy.table import EventTable
events = EventTable.fetch_open_data(
    "GWTC-1-confident",
    columns=("mass1", "mass2", "E_rad", "distance"),
)