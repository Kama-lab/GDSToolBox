import sqlite3

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
    'Alaska':'AS',
    'Oman Air':'WY'
}



try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    i=2
    for key in airlines_list:
        print()
        query = f"INSERT INTO toolbox_airline (id,name,code) VALUES ({i},'{key}','{airlines_list[key]}')"
        count = cursor.execute(query)
        sqliteConnection.commit()
        i+=1
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
