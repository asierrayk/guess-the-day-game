from string import Template

DMY_FORMAT = ['day', 'month', 'year']
YMD_FORMAT = ['year','month', 'day']
YDM_FORMAT = ['year', 'day', 'month']

# DMY_FORMAT = '%d %b %Y'
# YMD_FORMAT = '%Y %m %d'
# YDM_FORMAT = '%Y %d %m'

date_formats = {
                'DMY': DMY_FORMAT,
                'YMD': YMD_FORMAT,
                'YDM': YDM_FORMAT}

day_formats = {
            'number': '%d'
}

year_formats = {
            'number': '%Y'
}

month_formats = {
                'number': '%m',
                'short': '%b',
                'long': '%B'
}

formats = {
            'day': day_formats,
            'month': month_formats,
            'year': year_formats
}

prepositions = {
                'es': ' de ',
                'en': ' of '
}

delimiters = {
                'blank': ' ',
                'comma': ',',
                'bar': '-',
                'slash': '/',
                'preposition': prepositions
}

def get_date_format(month_format = month_formats['short'],
                day_format = day_formats['number'],
                year_format = year_formats['number'],
                date_format = date_formats['DMY'],
                delimiter=delimiters['blank']):
    date_template = Template('$first$delimiter$second$delimiter$third')
    formats = {
            'day': day_format,
            'month': month_format,
            'year': year_format
    }

    l  = [formats[x] for x in date_format]
    return date_template.substitute(first=l[0],second=l[1],third=l[2], delimiter=delimiter)

