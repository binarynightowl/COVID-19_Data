"""
This example shows how to get just the COVID-19 data from the John Hopkins University if you would like to use the
data in your application for other purposes
"""

import json, urllib.request

# url to query to get the total of all the confirmed cases, deaths, and recovered cases in the world - check GitHub for
# more info
world_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases' \
            '/FeatureServer/1/query?where=1=1&outStatistics=[{%22statisticType%22:%22sum%22,' \
            '%22onStatisticField%22:%22Confirmed%22,%22outStatisticFieldName%22:%22confirmed%22},' \
            '{%22statisticType%22:%22sum%22,%22onStatisticField%22:%22deaths%22,' \
            '%22outStatisticFieldName%22:%22deaths%22},{%22statisticType%22:%22sum%22,' \
            '%22onStatisticField%22:%22recovered%22,%22outStatisticFieldName%22:%22recovered%22}]&f=pjson'
china_us_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query' \
               '?where=1=1&objectIds=18,4&outFields=%20Country_Region,%20confirmed,%20deaths,%20recovered,' \
               '%20active&returnGeometry=false&f=pjson'
state_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/1/query' \
            '?where=Country_Region=%27US%27&outFields=Province_State,confirmed,deaths,recovered,' \
            '%20active&resultRecordCount=200&f=pjson'


state_data = {
}


# get data for any state based on state name
def get_state_data(state_to_find):
    document = json.loads(urllib.request.urlopen(state_url).read().decode())['features']
    for state in document:
        state = state['attributes']
        if state['Province_State'] == state_to_find:
            state_data[state_to_find] = (state['Confirmed'] - state['Deaths'] - state['Recovered'])


# get data for all states in a given list and append it to the dictionary
def get_all_state_data():
    states = ["New York", "Washington", "New Jersey", "California", "Illinois", "Michigan", "Florida", "Louisiana",
              "Massachusetts", "Texas", "Georgia", "Colorado"]
    for state in states:
        get_state_data(state)



data = json.loads(urllib.request.urlopen(world_url).read().decode())  # scrape data from JSON Query

total_cases = data['features'][0]['attributes']['confirmed']
total_deaths = data['features'][0]['attributes']['deaths']
total_recovered = data['features'][0]['attributes']['recovered']
total = [total_cases, total_deaths, total_recovered]

data = json.loads(urllib.request.urlopen(china_us_url).read().decode())  # scrape data from new JSON Query

china_cases = data['features'][0]['attributes']['Confirmed']
china_deaths = data['features'][0]['attributes']['Deaths']
china_recovered = data['features'][0]['attributes']['Recovered']
china = [china_cases, china_deaths, china_recovered]

us_cases = data['features'][1]['attributes']['Confirmed']
us_deaths = data['features'][1]['attributes']['Deaths']
us_recovered = data['features'][1]['attributes']['Recovered']
us = [us_cases, us_deaths, us_recovered]

get_all_state_data()

print(total, china, us, state_data['Texas'])
