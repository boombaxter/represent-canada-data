from datetime import date

import boundaries

boundaries.register('Thunder Bay wards',
    domain='Thunder Bay, ON',
    last_updated=date(2012, 10, 25),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Thunder Bay',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3558004'},
)
