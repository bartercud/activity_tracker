import data
import datetime as dt
import csv
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def get_input():
    inputs = {"type": None, "name": None, "day":None, "quantity": None}
    cur = input("Would you like to log something you did today? (y/n)\n")
    if (list(cur)[0].lower() == "y"):
        print("\n")
        day = dt.date.today()
    elif (list(cur)[0].lower() =="n"):
        year = safe_inp("Enter year\n")
        print("\n")
        month = safe_inp("Enter month (number)\n")
        print("\n")
        given_day = safe_inp("Enter day (number)\n")
        print("\n")
        day = dt.date(year, month, given_day)
    else:
        print("Invalid Input")
        raise SystemExit

    type = safe_inp('(1) stat\n(2) activity\n')
    print("\n")

    if (type == 1):
        print("(1) steps\n(2) well being\n(3) floors\n(4) sleep")
        name = safe_inp("Choose one of the stats above\n")
        name = name + 13
        print("\n")

    else:
        print("(1) run\n(2) workout\n(3) duties\n(4) friends\n(5) s/o\n(6) entertainment\n(7) lectures\n(8) assignments\n(9) personal projects\n(10) family\n(11) vacation\n(12) teaching\n(13) lab work")
        print("\n")
        name = safe_inp("Choose one of the activitues above\n")
        print("\n")

    if ((type == 2) or (name == 17)):
        quantity = safe_inp("How many minutes did you do this for?\n")
        print("\n")

    if (name == 14):
        quantity = safe_inp("How many steps did you take?\n")
        print("\n")

    if (name == 16):
        quantity = safe_inp("How many floors did you climb?\n")
        print("\n")

    if (name == 15):
        take_survey()
        quantity = safe_inp("What was your score (Multiply score by 10)\n")
        print("\n")


    inputs["name"] = name
    inputs["type"] = type
    inputs["day"] = day
    inputs["quantity"] = quantity

    return inputs

def safe_inp(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

def make_obj():
    atts = get_input()
    obj = data.data(atts["name"], atts["quantity"], atts["type"], atts["day"])
    return obj

def log():
    item = make_obj()
    with open('info.csv', 'a+', newline = '') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow([item.day, item.name, item.quantity])

def take_survey():
    webbrowser.open('http://happiness-survey.com/')

def scale_data(dframe):
    '''
    #TODO: FIX THIS FUNCTION
    '''
    '''
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(dframe), columns=dframe.columns)
    return df_scaled
    '''

    scaled_features = dframe.copy()
    col_names = [num for num in range(1,18)]
    features = scaled_features[col_names]
    scaler = MinMaxScaler().fit(features.values)
    features = scaler.transform(features.values)
    scaled_features[col_names] = scaled_features
    return scaled_features

def show():
    df = pd.read_csv(r'info.csv',
                    parse_dates=[0])
    #print(df)

    numdays = 1000

    base = dt.date.today()
    date_list=[(base-dt.timedelta(days=x)) for x in range(numdays)]

    df2 = df[df['Date'].isin(date_list)]
    #print(df2)

    dates = df2.Date.unique()
    names = df2.Name.unique()

    #print(dates)
    #print(names)
    new_dates = []
    new_names = []
    for date in dates:
        for num in range(len(names)):
            new_dates.append(str((pd.to_datetime(date)).date()))
            new_names.append(num+1)

    #print(new_names)
    #print(new_dates)

    #print(new_dates)

    d = {'Date':[new_dates], 'Name': [new_names]}
    #d['Quantity'] = 0
    print(d)

    new_df = pd.DataFrame.from_dict(d)
    print(new_df)

    #for date in dates:
        #for name in names:
            #tot = df2.query(("Date"==date)&("Name"==name)).sum()



    #df2_wide = df2.pivot("Date", "Name", "Quantity")
    #print(df2_wide,"\n")

    #df3 = scale_data(df2_wide)
    #print(df3)

    #sns.lineplot(data=df3)
    #plt.show()
