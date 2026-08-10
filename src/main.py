import pandas

# todo: create regional dataset

# USA POPULATION: REGIONAL
print("\n====> USA-POPULATION-REGIONAL dataset\n")
# todo: top 5 most / top 5 least

# USA POPULATION: STATES
print("====> USA-POPULATION-STATES dataset\n")
df_states = pandas.read_csv("dataset/usa-population-states-2020.csv")

# top 5 most populated
print("top 5 most populated states")
print(df_states.sort_values(by="Population", ascending=False).head())

# top 5 least populated
print("\ntop 5 least populated states")
print(df_states.sort_values(by="Population").head())

print("") # lul