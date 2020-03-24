---
layout: default
---

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
    - This will return a JSON Document with the Total World Confirmed Cases, World Deaths, and World Recovered Cases, 
    which should look like this *(data will differ of course)*:
   