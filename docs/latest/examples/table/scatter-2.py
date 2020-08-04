plot = events.scatter(
    "mass_1_source", "mass_2_source",
    color="chirp_mass_source"
)
plot.colorbar(label="Chirp_mass [{}]".format(r"M$_{\odot}$"))
plot.show()