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
    cites=("chicago", "new york city", "washington")    
    while True:
        city=input("Enter the city from chicago,new york city,washington: ").lower()
        if city in cites:
            break
        else:
            print("error city")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all', 'january', 'february','march','april','may','june']    
    while True:
        month=input("Enter the month from all, january, february, ... , june: ").lower()
        if month in months:
            break
        else:
            print("erorr month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    while True:
        day=input("Enter the day from all, monday, tuesday, ... sunday: ").lower()
        if day in days:
            break
        else:
            print("erorr day")
              

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

def data_of_rows(df):
    i=0
    ans=input("if you like to display the first five rows? yes/no: ").lower()
    while True:
        if ans=="no":
            break
        else:
            print(df[i:i+5])
        ans=input("if you like to display the next five rows? yes/no: ").lower()
        i+=5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_most_common_month=df['month'].mode()[0]
    print("common month: ",the_most_common_month)
    # TO DO: display the most common day of week
    the_most_common_day_of_week=df['day'].mode()[0]
    print("common day: ",the_most_common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("common hour: ",popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df["start station"].mode()[0]
    print("the most commonly station: ",common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df["end station"].mode()[0]
    print("the most commonly station: ",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station=(df["start staion"]+" "+df["end station"]).mode()[0]
    print("the most frequent combination of start station and end station trip: ",common_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df["Trip Duration"].sum()
    print("the total travel time: ",total_time,'sec',total_time/3600)

    # TO DO: display mean travel time
    mean_time=df["Trip Duration"].mean()
    print("the mean travel time: ",mean_time,'sec',mean_time/3600)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of user types: ",df['user type'].value_counts())

    # TO DO: Display counts of gender
    print("count of user gender: ",df['gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year=df['birth year'].min()
    print("the earliest year of birth: ",earliest_year)
    recent_year=df['birth year'].max()
    print("the most recent year of birth: ",recent_year)
    common_year=df['birth year'].mode()[0]
    print("the common year of birth: ",common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
