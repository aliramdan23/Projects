import numpy as np
import time
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
    city = ['chicago','new york','washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = input('Which city would you like to explore: chicago, new york, or washington?:').lower()
            if city in CITY_DATA:
                print('Great!')
                break
            elif city not in CITY_DATA:
                print('Error: Please try again ') 
        except KeyError:
                       
            pass 
    # get user input for month (all, january, february, ... , june)
    
    while True: 
        try:
            month = input('What month would you like to filter by? enter month in full. otherwise enter "all": ').lower()
            if month in months:
                print('Great!')
                break
            elif month not in months :    
        
                print('\nError: Please try again\n')
        except KeyError:        
            pass    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True: 
        try:
            day = input('Which day would you like to filter by?  enter day in full. otherwise enter "all": ').lower()
            if day in days:
                print('Great!')
                break
            elif day not in days :    
            
                print('\nError: Please try again \n')

        except KeyError: 
            pass
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
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is ', most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The cost common day of week is ', most_common_day)
    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is ', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is ', most_common_start_station)
    
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is ', most_common_end_station)
    # display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combo = df['comb'].mode()[0]
    print('The most frequent combination of start and end station is ', most_common_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time of travel is {} seconds '.format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean time of travel is {} seconds'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    
    sus_count = user_type_count.iloc[0]
    print('There are {} users that are suscribers'.format(sus_count))
    
    cus_count = user_type_count.iloc[1]
    print('There are {} users that are customers'.format(cus_count))
    
    nouser_type_count = df['User Type'].isnull().sum()
    print('There are {} unidentified user types'.format(nouser_type_count))
    
    dep_type_count = df['User Type'].size - (sus_count + cus_count + nouser_type_count)
    print('There are {} users that are dependent'.format(nouser_type_count))
            
        # Display counts of gender
    gender_type_count = df['Gender'].value_counts()
        
    male_count = gender_type_count.iloc[0]
    print('There are {} males'.format(male_count))
        
    female_count = gender_type_count.iloc[1]
    print('There are {} females'.format(female_count))
        
    nogender_type_count = df['Gender'].isnull().sum()
    print('There are {} unidentified genders'.format(nogender_type_count))
        
    #Check for birth year column
        
        # Display earliest, most recent, and most common year of birth
    earliest_birthyear = df['Birth Year'].min()
    print('The earliest birth year is ', earliest_birthyear)
        
    most_recent_birthyear = df['Birth Year'].max()
    print('The most recent birth year is ', most_recent_birthyear)
        
    most_common_birthyear = df['Birth Year'].mode()[0]
    print('The most common birth year is ', most_common_birthyear)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
def display_data(df):
    
    #get user input for data displaying successive five rows of data at a time
    while True:
        i = 0
        j = 5     
        dat = input('Would you like to view the data? Enter yes or no\n')
        if dat.lower() == 'yes':
            df = df.iloc[i:j]
            print('These are the first five rows of the data\n', df)  
            i += 1
            j += 1
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
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
    main()        