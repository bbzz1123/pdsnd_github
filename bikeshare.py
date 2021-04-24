import time
import numpy as np
import pandas as pd

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
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to explore? input in lowercase only: ")
        print ("Cool let's explore {}!".format(city.title())) 
   
        if city not in CITY_DATA.keys():
            print("Invalid input!")
            print("Please choose from: chicago, washington, and new york city")
            continue
        else: 
            break
 
    # get user input for month (all, january, february, ... , june)
    month = input("Which month do you want to investigate for your city of choice? \n Choose between january to june? Or all?:  ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week? \n monday-sunday? Or all?:  ")

    print('-'*40)
    return city, month, day
                      
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df["dow"] = df["Start Time"].dt.day_name #dow = day of week

    if month != 'all':
        month = ['january', 'february','march', 'april', 'may','june']
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    com_month = df['month'].mode()[0] #display the first element of the result
    print(com_month)

    # display the most common day of week
    df['dow'] = df['Start Time'].dt.week
    com_dow = df['dow'].mode()[0]
    print(com_dow)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hr = df['hour'].mode()[0] 
    print(com_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    df['start'] = df['Start Station']
    com_start = df['start'].mode()[0]

    # display most commonly used end station
    df['end'] = df['End Station']
    com_start = df['end'].mode()[0]

    # display most frequent combination of start station and end station trip
    
    df['start_end'] = df['Start Station'] + df['End Station']
    com_trip = df['start_end'].mode()[0]  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['totaltime'] = df['Trip Duration'] 
    total_travel_time = df['totaltime'].sum()
    print(total_travel_time)


    # display mean travel time
    mean_time = df['totaltime'].mean()
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df['users'] = df['User Type']
    user_type = df['users'].value_counts()
    print(user_type)
    # Display counts of gender   
    if 'Gender' in df:
        df['gender'] = df['Gender']
        gender = df['gender'].value_counts()
        print(gender)
    else:
        print('No gender data in this city')
        
    # Display earliest, most recent, and most common year of birth
    if 'Birth_year' in df:
        df['birth'] = df['Birth Year']
        earliest = df['birth'].min()
        recent = df['birth'].man()
        common = df['birth'].mode()[0]
        print("Birth year data:", earliest, recent, common)
    else:
       print('No Birth year data in this city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df

#display certain rows of raw data and limit to 5 rows at a time.
def display_data(df):
    view_data = input ('Would you like to view indivdual trip data? \n yes or no?: ')
    start_loc = 0
    view_display = 'yes'
    while view_display == 'yes':
        print(df.iloc[start_loc:start_loc +5])
        start_loc +=5
        view_display = input ('Do you want to view more data?: yes or no?: ')
        
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
               
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data (df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
                         
if __name__ == "__main__":
	main()
    
