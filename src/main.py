import pandas

regions = {

    # coastal

    "East Coast": [
        "Maine",
        "New Hampshire",
        "Vermont",
        "Massachusetts",
        "New York",
        "Connecticut",
        "Rhode Island",
        "Pennsylvania",
        "New Jersey",
        "Maryland",
        "Delaware",
        "West Virginia",
        "Virginia",
        "North Carolina",
        "South Carolina",
        "Georgia",
        "Florida"
    ],
    "Great Lakes": [
        "Wisconsin",
        "Illinois",
        "Indiana",
        "Michigan",
        "Ohio"
    ],
    "Gulf Coast": [
        "Texas",
        "Louisiana",
        "Mississippi",
        "Alabama",
        "Florida"
    ],
    "West Coast": [
        "Washington",
        "Oregon",
        "California"
    ],

    # coastal (custom)

    "East Coast (north)": [
        "Maine",
        "New Hampshire",
        "Vermont",
        "Massachusetts",
        "New York",
        "Connecticut",
        "Rhode Island",
        "Pennsylvania",
        "New Jersey",
        "Maryland",
        "Delaware",
        "West Virginia",
        "Virginia"
    ],

    "East Coast (south)": [
        "North Carolina",
        "South Carolina",
        "Georgia",
        "Florida"
    ],

    # w/ other

    "other": [
        "Alaska",
        "Arizona",
        "Arkansas",
        "Colorado",
        "Hawaii",
        "Idaho",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Minnesota",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Mexico",
        "North Dakota",
        "Oklahoma",
        "South Dakota",
        "Tennessee",
        "Utah",
        "Wyoming"
    ]

}

df_states = pandas.read_csv("dataset/usa-population-states.csv")

# coastal
population_eastcoast = df_states.loc[df_states["State"].isin(regions["East Coast"]), "Population"].sum()
population_greatlakes = df_states.loc[df_states["State"].isin(regions["Great Lakes"]), "Population"].sum()
population_gulfcoast = df_states.loc[df_states["State"].isin(regions["Gulf Coast"]), "Population"].sum()
population_westcoast = df_states.loc[df_states["State"].isin(regions["West Coast"]), "Population"].sum()

# coastal (custom)
population_eastcoast_north = df_states.loc[df_states["State"].isin(regions["East Coast (north)"]), "Population"].sum()
population_eastcoast_south = df_states.loc[df_states["State"].isin(regions["East Coast (south)"]), "Population"].sum()

# w/ other
population_other = df_states.loc[df_states["State"].isin(regions["other"]), "Population"].sum()

df_population_regions = pandas.DataFrame(
    columns=[
        "Region",
        "Population"
    ]
).astype(
    {
        "Region": "string",
        "Population": "int64"
    }
)
df_population_regions.loc[len(df_population_regions)] = ["East Coast", population_eastcoast]
df_population_regions.loc[len(df_population_regions)] = ["Great Lakes", population_greatlakes]
df_population_regions.loc[len(df_population_regions)] = ["Gulf Coast", population_gulfcoast]
df_population_regions.loc[len(df_population_regions)] = ["West Coast", population_westcoast]
# ===> save
df_population_regions.to_csv("dataset/usa-population-regions.csv", index=False)
print("✓ created usa-population-regions.csv")

df_population_regions_custom = pandas.DataFrame(
    columns=[
        "Region[custom]",
        "Population"
    ]
).astype(
    {
        "Region[custom]": "string",
        "Population": "int64"
    }
)
df_population_regions_custom.loc[len(df_population_regions_custom)] = ["East Coast (north)", population_eastcoast_north]
df_population_regions_custom.loc[len(df_population_regions_custom)] = ["East Coast (south)", population_eastcoast_south]
df_population_regions_custom.loc[len(df_population_regions_custom)] = ["Great Lakes", population_greatlakes]
df_population_regions_custom.loc[len(df_population_regions_custom)] = ["Gulf Coast", population_gulfcoast]
df_population_regions_custom.loc[len(df_population_regions_custom)] = ["West Coast", population_westcoast]
# ===> save
df_population_regions_custom.to_csv("dataset/usa-population-regions_custom.csv", index=False)
print("✓ created usa-population-regions_custom.csv")

df_population_regions_custom_other = pandas.DataFrame(
    columns=[
        "Region[custom w/ other]",
        "Population"
    ]
).astype(
    {
        "Region[custom w/ other]": "string",
        "Population": "int64"
    }
)
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["East Coast (north)", population_eastcoast_north]
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["East Coast (south)", population_eastcoast_south]
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["Great Lakes", population_greatlakes]
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["Gulf Coast", population_gulfcoast]
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["West Coast", population_westcoast]
df_population_regions_custom_other.loc[len(df_population_regions_custom_other)] = ["other", population_other]
# ===> save
df_population_regions_custom_other.to_csv("dataset/usa-population-regions_custom_other.csv", index=False)
print("✓ created usa-population-regions_custom_other.csv")