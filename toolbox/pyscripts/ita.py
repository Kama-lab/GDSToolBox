import re

airlines_list = {
    'American':'AA',
    'Delta':'DL',
    'Air Canada':'AC',
    'United':'UA',
    'British Airways':'BA',
    'Eva Air':'BR',
    'Brussels Airlines':'SN',
    'SWISS':'LX',
    'Lufthansa':'LH',
    'Alitalia':'AZ',
    'Air France':'AF',
    'KLM':'KL',
    'EgyptAir':'MS',
    'Philippine Airlines':'PR',
    'Southwest':'WN',
    'Turkish Airlines':'TK',
    'Ethiopian':'ET',
    'JAL':'JL',
    'Singapore Airlines':'SQ',
    'ANA':'NH',
    'Aer Lingus':'EI',
    'Finnair':'AY',
    'Kenya Airways':'KQ',
    'Iberia':'IB',
    'Vistara':'UK',
    'Air India':'AI',
    'Air Algerie':'AH',
    'Qatar Airways':'QR',
    'Tap Air Portugal':'TP',
    'Royal Air Maroc':'AT',
    'EVA Air':'BR',
    'Asiana':'OZ',
    'Etihad':'EY',
    'Korean Air':'KE',
    'Jeju Air':'7C',
    'Cayman Airways':'KX',
    'Evelop airlines':'E9',
    'JetBlue':'B6',
    'Kuwait Airways': 'KU',
    'SriLankan':'UL',
    'Alaska':'AS'
}





def validate_time(time):
    strings = time.split(' ')
    daynight = 'A' if strings[2][0].casefold() == 'a'.casefold() else 'P'
    return strings[1].replace(':','')+daynight



def contains_fl_details(flight_route,details):
    flight_details = []
    info_order = 0

    airlines_name_code,booking_class,d_day_n,d_month,route_code,dep_time,arr_time,d_weekday = (None,)*8

    route_code_pattern = re.compile(r'\([A-Z]{3}\)')
    dep_day = re.compile('([m|M]on|[t|T]ue|[w|W]ed|[t|T]hu||[f|F]ri|[s|S]at]|[s|S]un),')
    dep_date = re.compile('([j|J]an|[f|F]eb|[m|M]ar|[a|A]pr|[m|M]ay|[j|J]un|[j|J]ul|[a|A]ug|[s|S]ep|[o|O]ct|[n|N]ov|[d|D]ec) \d{1,2}')
    airlines = re.compile('([a-zA-Z]* ){1,3}\d{,4}$')
    dep = re.compile('[Dd]ep')
    arr = re.compile('[Aa]rr')
    b_class = re.compile('\([a-zA-Z]\)')
    arr_day = re.compile('[a-zA-Z]{3},')
    for line in details:
        if info_order == 0 and airlines.search(line):
            try:
                airlines_name, airlines_code = airlines.search(line).group(0).rsplit(' ',1)
                airlines_name_code = airlines_list[airlines_name] + ' '*(4-len(airlines_code)) + str(airlines_code)
                if len(airlines_name_code) == 6:
                    info_order+=1
            except ValueError:
                pass
            except AttributeError:
                pass
            except KeyError:
                print(airlines_name," is not found")
                exit()
        if info_order == 1 and dep.search(line):
            dep_time = validate_time(line)
            info_order+=1
        if info_order == 2 and arr.search(line):
            arr_time = validate_time(line)
            info_order+=1
        if info_order == 3 and b_class.search(line):
            booking_class = b_class.search(line).group(0)[1]
            info_order+=1
        if info_order == 4:
            d_day = dep_day.search(flight_route)
            d_date = dep_date.search(flight_route)
            if d_day and d_date:
                d_weekday = d_day.group(0)[:2]
                d_month,d_day_n = d_date.group(0).split(' ')
                info_order+=1
        if info_order == 5:
            route_code = re.findall(route_code_pattern,flight_route)
            if route_code:
                route_code = ''.join(route_code).replace('(','').replace(')','')
                info_order+=1

    flight_details = [airlines_name_code,
                    booking_class,
                    d_day_n,
                    d_month,
                    route_code,
                    dep_time,
                    arr_time,
                    d_weekday
                    ]
    if all(flight_details):
        return flight_details
    else:
        return False



def convert_to_gds(line,input_type):
    line.append("--------------------")
    if not (input_type == "ita"):
        return False
    pattern = re.compile(r'\([A-Z]{3}\)')
    seg_ind = []
    segments = []
    seg_details = []
    n=0
    for seg in line:
        if pattern.search(seg):
            if len(seg_ind) == 0:
                seg_ind.append(seg)
            else:
                seg_details_processed = contains_fl_details(seg_ind[0],seg_details)
                if seg_details_processed:
                    seg_details.insert(0,seg_ind[0])
                    segments.append(seg_details_processed)
                    seg_details = []

                seg_ind = [seg]
        elif n==(len(line)-1):
            seg_details_processed = contains_fl_details(seg_ind[0],seg_details)
            if seg_details_processed:
                seg_details.insert(0,seg_ind[0])
                segments.append(seg_details_processed)
                seg_details = []
        else:
            seg_details.append(seg)
        n+=1

    [segments[n].insert(0,n+1) for n in range(len(segments))]
    spaces = lambda x,l: str(' ')*(x-len(l))
    def format_segments(s):
        return ''.join([f'{s[0]} {s[1]}{s[2]} ',
        f'{str(0)*(2-len(s[3]))}',
        f'{s[3]}{s[4]} {s[5]} SS1',
        f'{spaces(7,s[6])}',
        f'{s[6]}',
        f'{spaces(6,s[7])}',
        f'{s[7]}']).upper()


    final_format = '\n'.join(list(map(format_segments,segments)))
    print(final_format)
    return final_format
