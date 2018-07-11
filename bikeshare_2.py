import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    usa = ['washington','chicago','new york city']
    mon= ['january','february','march','april','may','june']
    options=['month','day','none']
    week= {'Sunday':'Sunday',
           'Monday':'Monday',
           'Tuesday':'Tuesday',
           'Wednesday':'Wednesday',
           'Thursday':'Thursday',
           'Friday':'Friday',
           'Saturday':'Saturday'}
    print('\nWelcome to the Bikeshare interactive screen!')
    city = str(input("Which City would you like to choose? (chicago,washington,new york city)\n"))
    if city in usa :
        print('Thanks for the city name')
    else:
        print("oops! Wrong city")
    
    
    opti= str(input("Choose ur desired option month,day or none:-\n"))
    global month
    global day
    #filters by month and day
    while opti==options[0]:
        month = str(input("Please select the month - january,february,march,april,may,june:-\n"))
        if month in mon:
            day=str(input("Please select the day (ex:-Thursday):-\n"))
            if day in week:
              print("Thanks")
              break
            else:
              print("oops! wrong day")
              break
        else:
            print("Please specify a valid one")
    #filters by day        
    while opti==options[1]:
        month='none'
        day=str(input("Please select the day  (ex:-Thursday):-\n"))
        if day in week:
            print("Thanks for the details")
            break
        else:
                print("Wrong day entered")
                break
    #No filters
    while opti==options[2]:
        month='none'
        day='none'
        print("Thanks for not filtering the analyzed data")
        break
    return city, month,day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','december']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day of week if applicable
    if day != 'none':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df
  
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("Computing User Statisitcs")
    # print value counts for each user type
    print("User Types are:\n")
    user_types = df['User Type'].value_counts()
    print(user_types)
    if city !='washington':
        print("\nGender Count:\n")
        gender= df['Gender'].value_counts()
        print(gender)
    else:
        print(" Gender data is currently unavailable for Washington")
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("Computing Time statistics\n")
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    # display the most common day of week
    kf = pd.read_csv(CITY_DATA[city])
    kf['Start Time'] = pd.to_datetime(kf['Start Time'])
    kf['day_of_week'] = kf['Start Time'].dt.weekday_name
    common_day = kf['day_of_week'].mode()[0]
    print('Most common day:',common_day)
    #display the most common month of week
    ff = pd.read_csv(CITY_DATA[city])
    ff['Start Time'] = pd.to_datetime(ff['Start Time'])
    ff['month']= ff['Start Time'].dt.month
    common_month = ff['month'].mode()[0]
    print('Most common month:',common_month)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    #display most commonly used start station
    most_start_station=df['Start Station'].mode()[0]
    print ("Most Common Start station:",most_start_station)
    # display most commonly used end station
    most_end_station=df['End Station'].mode()[0]
    print("Most Common End station:",most_end_station)
    
    # display most frequent combination of start station and end station trip
    print("Common Start and End station:-")
    df['pop_trip']=df['Start Station'] + df['End Station']
    common_trip = df['pop_trip'].mode()[0]
    print(common_trip)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    # display total travel time
    travel_time=df['Trip Duration'].values.sum() 
    print("Total Travel time:",travel_time)
    # display mean travel time
    mean_time=df['Trip Duration'].values.mean()
    print("Average Travel Time:",mean_time)
    
def birth_year_stats(df):
    # Display earliest, most recent, and most common year of birth
    #recent birth year
    if city != 'washington':
        df=df.sort_values(by='Birth Year', ascending=False)
        birth = df.iloc[0]
        print("\nRecent Birth Year:-\n")
        print(birth)
        #earliest birth year
        df=df.sort_values(by='Birth Year', ascending=True)
        birth_early = df.iloc[0]
        print("\nEarliest Birth Year:-\n")
        print(birth_early)
        #Common Birth year
        common_birth_year=df['Birth Year'].mode()[0]
        print("\nCommon Birth Year:",common_birth_year)
    else:
        print(" Birth year statistics are not available for Washington")

#Functions called to run the program
city, month, day = get_filters()
df = load_data(city, month, day)
user_stats(df)
time_stats(df)
station_stats(df)
trip_duration_stats(df)
birth_year_stats(df)




     

      
 