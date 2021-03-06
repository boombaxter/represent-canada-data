from datetime import date

import boundaries

boundaries.register('Clarington wards',
    domain='Clarington, ON',
    last_updated=date(2012, 11, 15),
    name_func=boundaries.attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Ward')),
    authority='Municipality of Clarington',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3518017'},
)
