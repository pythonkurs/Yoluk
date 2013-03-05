from __future__ import division
import urllib,untangle
def NYC_outage_fraction ():
    print 'Getting the data from : http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
    f=urllib.urlopen('http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml')
    print 'Data collection is done'
    raw_data=f.read()
    print 'Parsing the data'
    raw_data_parse=untangle.parse(raw_data)
    raw_data_parse.get_elements()

    print 'Filtering the outage data'

    outages = raw_data_parse.NYCOutages.outage

    global total
    total=len(outages)

    print 'Total nr. of escalators ' +str(total)

    global repair
    repair = 0
    for outage in outages:
        outage.get_elements()
        reason=outage.reason.cdata
        if reason == 'REPAIR':
            repair=+1
        else:
            continue

    print 'Nr. of escalators need repair ' + str(repair)

    global frac
    frac=repair/total*100

    print 'This is' +str(frac)+'% of the total escalators'
