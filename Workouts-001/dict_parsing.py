#Workouts

#Print the languages that are inferior to Python

py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}



print(py[''])


#print the items
#print the roles

junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}



wtf = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}

#Get the first array value for the key 2
#Print all the array value for the key 2
#Print value of key 'a','b','c','d','e'
#Print the sum of the array with key 'e'
#set value of key 'e' to ['Chera','Chola','Pandiya']

print(wtf['a']['b']['c']['d']['e'])
#Get the value Mats from the Dict

body = {
    'query': {
        'filtered': {
            'query': {
                'match': {'description': 'addictive'}
            },
            'filter': {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}

#Modify the below statement to print Mats
print(body["query"]['filtered']['filter'])


# print the IMDB star rating ( 6.7)
# print the length of the movie

movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [ {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                   {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"} ]
    }
}

print(movie_box["Robin Hood: Men in Tights"])
