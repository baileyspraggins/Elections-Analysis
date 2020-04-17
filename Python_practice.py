counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties but El Paso is not in the list of counties.")

for county in counties:
    print(county)
number = [0, 1, 2, 3, 4]
for num in number:
        print(num)
for i in range(len(counties)):
    print(counties[i])
counties_tuple = ("Arapahoe", "Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jeffersom": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, "has", voters, "registered voters.")
voting_data = [{"county":"Arapahoe","registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson","registered_voters": 432438}]

for i in range(len(counties_dict)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
        
for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])
dir(int)
dir(float)
import csv
dir(csv)
