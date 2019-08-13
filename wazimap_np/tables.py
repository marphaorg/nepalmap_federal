from wazimap.data.tables import FieldTable, SimpleTable

# Population tables
FieldTable(['sex'],
           id='population',
           universe='Population',
           description='Total Population',
           dataset='National Population and Housing Census 2011',
           year='2011')

FieldTable(['religion name'],
           id='religion',
           universe='Population',
           description='Population by Religion',
           dataset='National Population and Housing Census 2011',
           year='2011')

# Agriculture Tables
FieldTable(['Agricultural land use area'],
           id='agriculture_land_use',
           universe='Agriculture',
           description='Agriculture Land Use Area',
           dataset='National Portal',
           year='2011')

FieldTable(['Agricultural holdings size by land tenure'],
           id='agriculture_holding_size',
           universe='agriculture holdings',
           description='Agricultural Holdings Size By Land Tenure',
           dataset='National Portal',
           year='2011')

