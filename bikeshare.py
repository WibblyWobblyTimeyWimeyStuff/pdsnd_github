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
    
    cities = ['chicago', 'new york city', 'washington']
    months = ['none', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['None','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input('Which city\'s data do you wish to explore: ').lower()
        if city not in cities:
            print('Sorry, this is not a valid city name. Please choose between Chicago, New York City or Washington.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input('Select a month between Januaray and June (inclusive), if you want to filter by month or \'none\' if you don\'t wish to apply filters: ').lower()
        if month not in months:
            print('This is not a valid month, please enter a valid month between January and June (inclusive) i.e January or \'none\' should you not wish to apply any filters')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('Select the day of the week you wish to filter by or \'none\' if you don\'t wish to apply filters by day of the week: ').title()
        if day not in days:
            print('Sorry, this is not a valid day. Please enter a valid day i.e Monday or \'none\' should you not wish to apply any filters')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'none':
       df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month for travel is: ', common_month)

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print('The most common travel day of the week is: ', common_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour for travel is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print('The station at which the most number of trips commence is: ', common_startstation)

    # TO DO: display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print('The station at which the most number of trips end is: ', common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    stationcombination = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    frequent_stationcombination = stationcombination.mode()[0]
    print('The most frequent station combination is ', frequent_stationcombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    traveltime_sec = df['Trip Duration'].sum()
    traveltime_min = round(traveltime_sec/3600)

    print('The approximate total travel time in hours is: ', traveltime_min)

    # TO DO: display mean travel time
    traveltime_mean_sec = df['Trip Duration'].mean()
    traveltime_mean_min = round(traveltime_mean_sec/60)

    print('The approximate average travel time in minutes is: ', traveltime_mean_min)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].values
    subscriber_sum = (user_type == 'Subscriber').sum()
    customer_sum = (user_type == 'Customer').sum()
    print('There are ', subscriber_sum, ' subscribers.')
    print('There are ', customer_sum, ' customers.')

    # TO DO: Display counts of gender
    if ('Gender') not in df:
        print('Sorry! We don\'t have gender data for Washington')
    else:
        gender = df['Gender'].values
        gender_m = (gender == 'Male').sum()
        gender_f = (gender == 'Female').sum()
        print('The number of male users is: ', gender_m)
        print('The number of female users is: ', gender_f)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if ('Birth Year') not in df:
        print('Sorry! We don\'t have birth year data for Washington')
    else: 
        yob = df['Birth Year'].values
        mostrecent_yob = yob.max()
        earliest_yob = yob.min()
        print('The most recent year of birth is ', mostrecent_yob)
        print('The earliest year of birth is ', earliest_yob)
        print('The most common year of birth is {}'.format(df['Birth Year'].mode()[0]))
         
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """ View first few rows of data """
    
    while True: 
        view_data = input('Would you like to view a few rows of the raw data? (yes or no): ').lower()
        if view_data == 'yes':
            try: 
                n = int(input('How may rows of data (from the top) would you like to see?: '))
                print(df.head(n))
            except ValueError:
                    print('Please enter an integer.')
        else: 
            break
        

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

"""
Other resources used (besides udacity practice solutions):
https://stackoverflow.com/questions/66833367/user-input-from-defined-list-in-python
https://www.geeksforgeeks.org/how-to-perform-a-countif-function-in-python/
https://stackoverflow.com/questions/50192965/how-to-make-user-input-not-case-sensitive
https://www.w3schools.com/python/pandas/ref_df_idxmax.asp#:~:text=The%20idxmax()%20method%20returns,maximum%20value%20for%20each%20row.
"""