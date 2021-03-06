#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Québec boroughs',
    domain=u'Québec, QC',
    last_updated=date(2013, 8, 20),
    name_func=boundaries.clean_attr('NOM'),
    id_func=boundaries.attr('CODE'),
    authority=u'Ville de Québec',
    source_url='http://donnees.ville.quebec.qc.ca/donne_details.aspx?jdid=2',
    licence_url='http://donnees.ville.quebec.qc.ca/licence.aspx',
    data_url='http://donnees.ville.quebec.qc.ca/Handler.ashx?id=2&f=SHP',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2423027'},
    prj='http://spatialreference.org/ref/epsg/4326/prj/',
)
