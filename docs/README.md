# COVID-19 Data Query
## Sources
This project utilizes [John Hopkins University](https://coronavirus.jhu.edu/map.html)'s 
[ArcGIS data layer](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) 
to get its data. The data layer pulls data from the following sources:
- [World Health Organization (WHO)](https://www.who.int/)
- [DXY.cn. Pneumonia. 2020.](http://3g.dxy.cn/newh5/view/pneumonia)
- [BNO News](https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/)
- [National Health Commission of the People’s Republic of China (NHC)](http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml)
- [China CDC (CCDC)](http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm)
- [Hong Kong Department of Health](https://www.chp.gov.hk/en/features/102465.html)
- [Macau Government](https://www.ssm.gov.mo/portal/)
- [Taiwan CDC](https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0)
- [US CDC](https://www.cdc.gov/coronavirus/2019-ncov/index.html)
- [Government of Canada](https://www.canada.ca/en/public-health/services/diseases/coronavirus.html)
- [Australia Government Department of Health](https://www.health.gov.au/news/coronavirus-update-at-a-glance)
- [European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases)
- [Ministry of Health Singapore (MOH)](https://www.moh.gov.sg/covid-19)
- [Italy Ministry of Health](http://www.salute.gov.it/nuovocoronavirus)

## Data Queries
I have provided some pre-defined queries (which return a JSON document) with the most helpful information set up and 
later I will explain how
 to 
create your own queries with custom filters, only specific data, etc. 
#### Pre-Defined Queries
1. Total World Confirmed Cases, World Deaths, and World Recovered Cases
    - URL: [World Data](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1=1&outStatistics=[{"statisticType":"sum","onStatisticField":"Confirmed","outStatisticFieldName":"confirmed"},{"statisticType":"sum","onStatisticField":"deaths","outStatisticFieldName":"deaths"},{"statisticType":"sum","onStatisticField":"recovered","outStatisticFieldName":"recovered"}]&f=pjson) *(Use this in your program to get the JSON Document)*
    - This will return a JSON Document with the worldwide total confirmed cases, deaths, and recoveries, 
    which should look like this *(data will differ of course)*:
        - <details>
            <summary>Click to reveal!</summary>
            
                {
                  "objectIdFieldName" : "OBJECTID", 
                  "uniqueIdField" : 
                  {
                    "name" : "OBJECTID", 
                    "isSystemMaintained" : true
                  }, 
                  "globalIdFieldName" : "", 
                  "geometryType" : "esriGeometryPoint", 
                  "spatialReference" : {
                    "wkid" : 4326, 
                    "latestWkid" : 4326
                  }, 
                  "fields" : [
                    {
                      "name" : "confirmed", 
                      "type" : "esriFieldTypeDouble", 
                      "alias" : "confirmed", 
                      "sqlType" : "sqlTypeFloat", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "deaths", 
                      "type" : "esriFieldTypeDouble", 
                      "alias" : "deaths", 
                      "sqlType" : "sqlTypeFloat", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "recovered", 
                      "type" : "esriFieldTypeDouble", 
                      "alias" : "recovered", 
                      "sqlType" : "sqlTypeFloat", 
                      "domain" : null, 
                      "defaultValue" : null
                    }
                  ], 
                  "features" : [
                    {
                      "attributes" : {
                        "confirmed" : 398107, 
                        "deaths" : 17454, 
                        "recovered" : 103334
                      }
                    }
                  ]
                }                               
          </details>

2. Total Cases, Deaths, and Recoveries by state
    - URL: [US-Data](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/1/query?where=Country_Region=%27US%27&outFields=Province_State,confirmed,deaths,recovered,%20active&resultRecordCount=200&f=pjson) *(Use this in your program to get the JSON Document)*
    - This will return a JSON Document with the total cases, deaths, and recoveries by state, 
    which should look like this *(data will differ of course)*:
        - <details>
            <summary>Click to reveal!</summary>
            
                {
                  "objectIdFieldName" : "OBJECTID", 
                  "uniqueIdField" : 
                  {
                    "name" : "OBJECTID", 
                    "isSystemMaintained" : true
                  }, 
                  "globalIdFieldName" : "", 
                  "geometryType" : "esriGeometryPoint", 
                  "spatialReference" : {
                    "wkid" : 4326, 
                    "latestWkid" : 4326
                  }, 
                  "fields" : [
                    {
                      "name" : "Province_State", 
                      "type" : "esriFieldTypeString", 
                      "alias" : "Province/State", 
                      "sqlType" : "sqlTypeOther", 
                      "length" : 8000, 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Confirmed", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Confirmed", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Deaths", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Deaths", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Recovered", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Recovered", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Active", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Active", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }
                  ], 
                  "features" : [
                    {
                      "attributes" : {
                        "Province_State" : "Mississippi", 
                        "Confirmed" : 320, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -89.678695999999945, 
                        "y" : 32.74164600000006
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Grand Princess", 
                        "Confirmed" : 28, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -122.66547899999995, 
                        "y" : 37.648940000000039
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Oklahoma", 
                        "Confirmed" : 106, 
                        "Deaths" : 3, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -96.928916999999956, 
                        "y" : 35.565342000000044
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Delaware", 
                        "Confirmed" : 91, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -75.507140999999933, 
                        "y" : 39.318523000000027
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Minnesota", 
                        "Confirmed" : 261, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -93.900191999999947, 
                        "y" : 45.694454000000064
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Illinois", 
                        "Confirmed" : 1535, 
                        "Deaths" : 16, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -88.986136999999985, 
                        "y" : 40.349457000000029
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Arkansas", 
                        "Confirmed" : 218, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -92.373122999999964, 
                        "y" : 34.969704000000036
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "New Mexico", 
                        "Confirmed" : 83, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -106.24848199999997, 
                        "y" : 34.840515000000039
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Indiana", 
                        "Confirmed" : 367, 
                        "Deaths" : 12, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -86.258277999999962, 
                        "y" : 39.849426000000051
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Louisiana", 
                        "Confirmed" : 1388, 
                        "Deaths" : 46, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -91.867804999999976, 
                        "y" : 31.169546000000025
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Texas", 
                        "Confirmed" : 897, 
                        "Deaths" : 12, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -97.563460999999961, 
                        "y" : 31.054487000000051
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Wisconsin", 
                        "Confirmed" : 481, 
                        "Deaths" : 5, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -89.616507999999953, 
                        "y" : 44.268543000000079
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Kansas", 
                        "Confirmed" : 100, 
                        "Deaths" : 2, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -96.726485999999966, 
                        "y" : 38.52660000000003
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "American Samoa", 
                        "Confirmed" : 0, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -170.13199999999998, 
                        "y" : -14.270999999999958
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Connecticut", 
                        "Confirmed" : 618, 
                        "Deaths" : 12, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -72.755370999999968, 
                        "y" : 41.597782000000052
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Virgin Islands", 
                        "Confirmed" : 17, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -64.89629999999994, 
                        "y" : 18.335800000000063
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "California", 
                        "Confirmed" : 2511, 
                        "Deaths" : 50, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -119.68156399999998, 
                        "y" : 36.116203000000041
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Puerto Rico", 
                        "Confirmed" : 39, 
                        "Deaths" : 2, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -66.59009999999995, 
                        "y" : 18.220800000000054
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Georgia", 
                        "Confirmed" : 1026, 
                        "Deaths" : 32, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -83.643073999999956, 
                        "y" : 33.040619000000049
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "North Dakota", 
                        "Confirmed" : 34, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -99.784011999999962, 
                        "y" : 47.528912000000048
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Pennsylvania", 
                        "Confirmed" : 946, 
                        "Deaths" : 8, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -77.209754999999973, 
                        "y" : 40.590752000000066
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "West Virginia", 
                        "Confirmed" : 22, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -80.954452999999944, 
                        "y" : 38.49122600000004
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Alaska", 
                        "Confirmed" : 34, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -152.40441899999996, 
                        "y" : 61.370716000000073
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Tennessee", 
                        "Confirmed" : 711, 
                        "Deaths" : 2, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -86.692344999999989, 
                        "y" : 35.747845000000041
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "United States Virgin Islands", 
                        "Confirmed" : 0, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -64.932999999999936, 
                        "y" : 18.350000000000023
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Missouri", 
                        "Confirmed" : 228, 
                        "Deaths" : 5, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -92.288367999999991, 
                        "y" : 38.45608500000003
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "South Dakota", 
                        "Confirmed" : 30, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -99.438827999999944, 
                        "y" : 44.29978200000005
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Colorado", 
                        "Confirmed" : 723, 
                        "Deaths" : 8, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -105.31110399999994, 
                        "y" : 39.059811000000025
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "New Jersey", 
                        "Confirmed" : 3675, 
                        "Deaths" : 44, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -74.521010999999987, 
                        "y" : 40.29890400000005
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Guam", 
                        "Confirmed" : 32, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : 144.79370000000006, 
                        "y" : 13.444300000000055
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Washington", 
                        "Confirmed" : 2221, 
                        "Deaths" : 111, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -121.49049399999996, 
                        "y" : 47.400902000000031
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "New York", 
                        "Confirmed" : 25677, 
                        "Deaths" : 210, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -74.948050999999964, 
                        "y" : 42.165726000000063
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Nevada", 
                        "Confirmed" : 278, 
                        "Deaths" : 4, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -117.05537399999997, 
                        "y" : 38.313515000000052
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Northern Mariana Islands", 
                        "Confirmed" : 0, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : 145.67390000000012, 
                        "y" : 15.097900000000038
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Diamond Princess", 
                        "Confirmed" : 49, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : 139.63800000000003, 
                        "y" : 35.443700000000035
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Maryland", 
                        "Confirmed" : 349, 
                        "Deaths" : 4, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -76.802100999999936, 
                        "y" : 39.063946000000044
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Idaho", 
                        "Confirmed" : 79, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -114.47882799999996, 
                        "y" : 44.240459000000044
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Wyoming", 
                        "Confirmed" : 29, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -107.30248999999998, 
                        "y" : 42.755966000000058
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Arizona", 
                        "Confirmed" : 326, 
                        "Deaths" : 5, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -111.431221, 
                        "y" : 33.729759000000058
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Iowa", 
                        "Confirmed" : 124, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -93.210525999999959, 
                        "y" : 42.011539000000027
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Michigan", 
                        "Confirmed" : 1793, 
                        "Deaths" : 24, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -84.536094999999989, 
                        "y" : 43.326618000000053
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Utah", 
                        "Confirmed" : 298, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -111.86243399999995, 
                        "y" : 40.150032000000067
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Virginia", 
                        "Confirmed" : 291, 
                        "Deaths" : 7, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -78.169967999999983, 
                        "y" : 37.769337000000064
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Oregon", 
                        "Confirmed" : 210, 
                        "Deaths" : 8, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -122.07093799999996, 
                        "y" : 44.572021000000063
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Montana", 
                        "Confirmed" : 46, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -110.45435299999997, 
                        "y" : 46.921925000000044
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "New Hampshire", 
                        "Confirmed" : 101, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -71.563895999999943, 
                        "y" : 43.452492000000063
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Massachusetts", 
                        "Confirmed" : 1159, 
                        "Deaths" : 11, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -71.530105999999932, 
                        "y" : 42.230171000000041
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "South Carolina", 
                        "Confirmed" : 298, 
                        "Deaths" : 5, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -80.945006999999976, 
                        "y" : 33.856892000000073
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Vermont", 
                        "Confirmed" : 95, 
                        "Deaths" : 7, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -72.710685999999953, 
                        "y" : 44.045876000000078
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Florida", 
                        "Confirmed" : 1412, 
                        "Deaths" : 18, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -81.686782999999934, 
                        "y" : 27.766279000000054
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Hawaii", 
                        "Confirmed" : 77, 
                        "Deaths" : 1, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -157.49833699999996, 
                        "y" : 21.094318000000044
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Kentucky", 
                        "Confirmed" : 123, 
                        "Deaths" : 4, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -84.67006699999996, 
                        "y" : 37.668140000000051
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Rhode Island", 
                        "Confirmed" : 124, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -71.511779999999987, 
                        "y" : 41.680893000000026
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Nebraska", 
                        "Confirmed" : 64, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -98.268081999999936, 
                        "y" : 41.125370000000032
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Ohio", 
                        "Confirmed" : 567, 
                        "Deaths" : 8, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -82.764914999999974, 
                        "y" : 40.388783000000046
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Alabama", 
                        "Confirmed" : 215, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -86.902299999999968, 
                        "y" : 32.318200000000047
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Wuhan Evacuee", 
                        "Confirmed" : 4, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : 5.6843418860808015E-14, 
                        "y" : 5.6843418860808015E-14
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "North Carolina", 
                        "Confirmed" : 479, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -79.806418999999948, 
                        "y" : 35.630066000000056
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "District of Columbia", 
                        "Confirmed" : 141, 
                        "Deaths" : 2, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -77.026816999999937, 
                        "y" : 38.897438000000079
                      }
                    }, 
                    {
                      "attributes" : {
                        "Province_State" : "Maine", 
                        "Confirmed" : 118, 
                        "Deaths" : 0, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }, 
                      "geometry" : 
                      {
                        "x" : -69.381926999999962, 
                        "y" : 44.693947000000037
                      }
                    }
                  ]
                }                            
          </details>


3. Total Cases, Deaths, and Recoveries in China and the US
    - URL: [China/US Data](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query?where=1=1&objectIds=18,4&outFields=%20Country_Region,%20confirmed,%20deaths,%20recovered,%20active&returnGeometry=false&f=pjson) *(Use this in your program to get the JSON Document)*
    - This will return a JSON Document with the cases, deaths, and recoveries in China and the US, 
    which should look like this *(data will differ of course)*:
        - <details>
            <summary>Click to reveal!</summary>
            
                {
                  "objectIdFieldName" : "OBJECTID", 
                  "uniqueIdField" : 
                  {
                    "name" : "OBJECTID", 
                    "isSystemMaintained" : true
                  }, 
                  "globalIdFieldName" : "", 
                  "geometryType" : "esriGeometryPoint", 
                  "spatialReference" : {
                    "wkid" : 4326, 
                    "latestWkid" : 4326
                  }, 
                  "fields" : [
                    {
                      "name" : "Country_Region", 
                      "type" : "esriFieldTypeString", 
                      "alias" : "Country_Region", 
                      "sqlType" : "sqlTypeOther", 
                      "length" : 8000, 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Confirmed", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Confirmed", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Deaths", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Deaths", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Recovered", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Recovered", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }, 
                    {
                      "name" : "Active", 
                      "type" : "esriFieldTypeInteger", 
                      "alias" : "Active", 
                      "sqlType" : "sqlTypeOther", 
                      "domain" : null, 
                      "defaultValue" : null
                    }
                  ], 
                  "features" : [
                    {
                      "attributes" : {
                        "Country_Region" : "China", 
                        "Confirmed" : 81591, 
                        "Deaths" : 3281, 
                        "Recovered" : 73280, 
                        "Active" : 5030
                      }
                    }, 
                    {
                      "attributes" : {
                        "Country_Region" : "US", 
                        "Confirmed" : 53268, 
                        "Deaths" : 696, 
                        "Recovered" : 0, 
                        "Active" : 0
                      }
                    }
                  ]
                }                              
          </details>