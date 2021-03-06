from datetime import date

import boundaries

boundaries.register('Brampton wards',
    domain='Brampton, ON',
    last_updated=date(2013, 1, 4),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUM'),
    id_func=boundaries.attr('WARDNUM'),
    authority='Regional Municipality of Peel',
    source_url='http://opendata.peelregion.ca/data-categories/regional-geography/ward-boundaries-(2010-2014).aspx',
    licence_url='http://opendata.peelregion.ca/terms-of-use.aspx',
    data_url='http://opendata.peelregion.ca/media/2549/wardboundary20102014_shp_04.2012.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3521010'},
    ogr2ogr='''-where "MUNIC='10'"''',
)
