# import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from itertools import combinations

def recode_round_to_ordinal(df):
    if df['tourney_level'] == 'A':
        if df['round'] == 'BR':
            resultat = 1
        elif df['round'] == 'RR':
            resultat = 2
        elif df['round'] == 'R64':
            resultat = 3
        elif df['round'] == 'R32':
            resultat = 4
        elif df['round'] == 'R16':
            resultat = 5
        elif df['round'] == 'QF':
            resultat = 6
        elif df['round'] == 'SF':
            resultat = 7 
        else:
            resultat = 8
            
    elif df['tourney_level'] == 'D' and df['round'] == 'RR':
        resultat = 1
          
    elif df['tourney_level'] == 'F':
        if df['round'] == 'BR':
            resultat = 1
        elif df['round'] == 'RR':
            resultat = 2
        elif df['round'] == 'SF':
            resultat = 3
        else:
            resultat = 4
            
    elif df['tourney_level'] == 'G':
        if df['round'] == 'R128':
            resultat = 1
        elif df['round'] == 'R64':
            resultat = 2
        elif df['round'] == 'R32':
            resultat = 3
        elif df['round'] == 'R16':
            resultat = 4
        elif df['round'] == 'QF':
            resultat = 5
        elif df['round'] == 'SF':
            resultat = 6
        else:
            resultat = 7

    elif df['tourney_level'] == 'M':
        if df['round'] == 'R128':
            resultat = 1
        elif df['round'] == 'R64':
            resultat = 2
        elif df['round'] == 'R32':
            resultat = 3
        elif df['round'] == 'R16':
            resultat = 4
        elif df['round'] == 'QF':
            resultat = 5
        elif df['round'] == 'SF':
            resultat = 6
        else:
            resultat = 7
    return resultat

def to_le(df,feature):
	# df[feature] = df[feature].astype(str)
    le = LabelEncoder()
    le.fit(df[feature])
    df[feature + "_labels_encoding"] = le.transform(df[feature])
    return df
