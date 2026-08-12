import pandas as pd

df_states = pd.read_csv("dataset/usa-population-states.csv")

# CREATE df_regions_coastal
df_regions_coastal = pd.DataFrame(columns=["Region(coastal)", "Population"]).astype({"Region(coastal)": "string", "Population": "int64"})

# rows for df_regions_coastal
row_eastcoast = df_states.loc[df_states["State"].isin(
    [
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
    ]
), "Population"].sum()
df_regions_coastal.loc[len(df_regions_coastal)] = ["East Coast", row_eastcoast]

row_greatlakes = df_states.loc[df_states["State"].isin(
    [
        "Wisconsin",
        "Illinois",
        "Indiana",
        "Michigan",
        "Ohio"
    ]
), "Population"].sum()
df_regions_coastal.loc[len(df_regions_coastal)] = ["Great Lakes", row_greatlakes]

row_gulfcoast = df_states.loc[df_states["State"].isin(
    [
        "Texas",
        "Louisiana",
        "Mississippi",
        "Alabama",
        "Florida"
    ]
), "Population"].sum()
df_regions_coastal.loc[len(df_regions_coastal)] = ["Gulf Coast", row_gulfcoast]

row_westcoast = df_states.loc[df_states["State"].isin(
    [
        "Washington",
        "Oregon",
        "California"
    ]
), "Population"].sum()
df_regions_coastal.loc[len(df_regions_coastal)] = ["West Coast", row_westcoast]

# print and create
print(f"\n{df_regions_coastal.head()}\n")
df_regions_coastal.to_csv("dataset/usa-population-regions-coastal.csv", index=False)

# CREATE df_regions_coastal_custom
df_regions_coastal_custom = pd.DataFrame(columns=["Region(coastal)[custom]", "Population"]).astype({"Region(coastal)[custom]": "string", "Population": "int64"})

# rows for df_regions_coastal_custom
row_eastcoast_north = df_states.loc[df_states["State"].isin(
    [
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
    ]
), "Population"].sum()
df_regions_coastal_custom.loc[len(df_regions_coastal_custom)] = ["East Coast north", row_eastcoast_north]

row_eastcoast_south = df_states.loc[df_states["State"].isin(
    [
        "North Carolina",
        "South Carolina",
        "Georgia",
        "Florida"
    ]
), "Population"].sum()
df_regions_coastal_custom.loc[len(df_regions_coastal_custom)] = ["East Coast south", row_eastcoast_south]

df_regions_coastal_custom.loc[len(df_regions_coastal_custom)] = ["Great Lakes", row_greatlakes]
df_regions_coastal_custom.loc[len(df_regions_coastal_custom)] = ["Gulf Coast", row_gulfcoast]
df_regions_coastal_custom.loc[len(df_regions_coastal_custom)] = ["West Coast", row_westcoast]

# print and create
print(f"{df_regions_coastal_custom.head()}\n")
df_regions_coastal_custom.to_csv("dataset/usa-population-regions-coastal-custom.csv", index=False)

# USA-POPULATION-REGIONAL dataset
print("====> USA-POPULATION-REGIONAL dataset\n")

print("top 5 most populated regions(coastal)")
print(f"{df_regions_coastal.sort_values(by='Population', ascending=False).head()}\n")

print("top 5 least populated regions(coastal)")
print(f"{df_regions_coastal.sort_values(by='Population').head()}\n")

print("top 5 most populated regions(coastal)[custom]")
print(f"{df_regions_coastal_custom.sort_values(by='Population', ascending=False).head()}\n")

print("top 5 least populated regions(coastal)[custom]")
print(f"{df_regions_coastal_custom.sort_values(by='Population').head()}\n")

# USA-POPULATION-STATES dataset
print("====> USA-POPULATION-STATES dataset\n")

# top 5 most populated
print("top 5 most populated states")
print(f"{df_states.sort_values(by='Population', ascending=False).head()}\n")

# top 5 least populated
print("top 5 least populated states")
print(f"{df_states.sort_values(by='Population').head()}\n")