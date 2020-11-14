import time
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
   
    
    while True:
        city = input('Please select Chicago, New York City or Washington data set:').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("invalid input")
            
            
    
    # TO DO: get user input for month (all, january, february, ... , june)

    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input( 'Enter the month:').lower()
        if month in month_list:
          break
        else:
            print("invalid input")


   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]
    while True:
        day = input('Enter the day:').lower()
        if day in day_list:
            break
        else:
            print("invalid input")
              
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays Statistics On the Most Trequent Times Of Travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is:', common_day)
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays Statistics On the most Popular Stations and Trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common start station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print('Common end station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + 'to' + df['End Station']
    common_start_end_station = df['start_end'].mode()[0]
    print('Most frequent start and end station is:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration =df['Trip Duration'].sum()
    print('The total travel time is:', trip_duration)

    # TO DO: display mean travel time
    mean_duration =df['Trip Duration'].mean()
    print('The mean of the travel time is:', mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertypes = df['User Type'].value_counts()
    print('Count of user types is:', count_usertypes)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       
        count_gender = df['Gender'].value_counts()
        print('Count of gender is:', count_gender)
    else:
        print('there is no data for this city') 
      
           

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       
        earliest =df['Birth Year'].min()
        most_recent= df['Birth Year'].max()
        most_common= df['Birth Year'].mode()[0]
        print('The earliest birth day is:', earliest)
        print('The most recent birth day is:', most_recent)
        print('The most common birth year is:', most_common)
    else:
        print('there is no data for this city') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    counter = 5
    while True:
        choice = input('do you want to see raw data?')
        if choice.lower() == 'yes' or choice.lower() == 'no':
            break
        else:
            print("invalid input")

    while choice.lower() == 'yes' or choice.lower() == 'no':       
        if choice.lower() == 'yes':
            print(df.iloc[counter : counter + 5])
            counter += 5
            choice = input('\ndo you want to see more raw data?')
        else:
            break
            
            
   # use to ask all functions to run

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
