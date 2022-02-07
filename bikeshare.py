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
    cities=CITY_DATA.keys()
    city=input("Enter the city (chicago, new york city, washington):").lower()
    while city not in cities:
        city=input("Enter the city (chicago, new york city, washington):").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    month=input("Enter the month: ").lower()
    while month not in months:
        month=input("Enter the month: ").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input("Enter the day:").lower()
    while day not in days:
        day=input("Enter the day:").lower()
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
    df=pd.read_csv(CITY_DATA[city])
    months=['january','february','march','april','may','june']
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    df['Start Time']=pd.to_datetime(df['Start Time'])
    if month!='all':
        month_val=months.index(month)+1
        df=df[df['Start Time'].dt.month==month_val]
    if day!='all':
        df=df[df['Start Time'].dt.weekday_name==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month :",df['Start Time'].dt.month.mode()[0])

    # TO DO: display the most common day of week
    print("the most common day of week :",df['Start Time'].dt.weekday_name.mode()[0])

    # TO DO: display the most common start hour
    print("the most common start hour :",df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station: ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("most commonly used End station: ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip",df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time :",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("mean travel time :",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types: ",df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("counts of gender: ",df['Gender'].value_counts())
    else:
        print("The gender column does not exists in this dataframe")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest=str(df['Birth Year'].tail(1)).split("   ")
        print("most earliest year of birth: ",earliest[1][0:5])
        recent=str(df['Birth Year'].head(1)).split("   ")
        print("most recent year of birth: ",recent[1][0:5])
        print("most common year of birth: ",df['Birth Year'].mode()[0])
    else:
        print("The birth year column does not exists in this dataframe")
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
        else:
            print(df.head())
            c=10
            while restart.lower()=='yes':
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                print(df.head(c))
                c+=5
            
if __name__ == "__main__":
	main()
