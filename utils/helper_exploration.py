import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# from this project
import utils.common as common

def check_target_distribution(df_clean):

        current_ax = plt.gca()
        sns.set_style('whitegrid')

        sns.countplot(x='ARR_DEL15', hue='ARR_DEL15', data=df_clean, ax=current_ax)

        plt.title('Flight Delay VS On Time')
        plt.xlabel('Arrival Delay')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.legend()

        plt.show()
        #common.save_fig('Flight Delay VS On Time', file_path)

def explore_flight_date_vs_delay(df_clean):

    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 5))
    order = np.unique(list(df_clean['FL_DATE'].iloc[:445827]))
    sns.barplot(x='FL_DATE', y='ARR_DEL15', data=df_clean.iloc[:445827], color="blue", order=order, estimator=np.sum)
    plt.xticks(rotation=90)
    plt.title("Flight Date Vs Total number of delayed flights ")
    plt.xlabel('FlightDate')
    plt.ylabel('Total number of delayed flights')
    plt.tight_layout()
    plt.show()

    # common.save_fig('Flight Date Vs Total number of delayed flights ', file_path)

    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 5))
    order = np.unique(list(df_clean['FL_DATE'].iloc[:445827]))
    sns.barplot(x='FL_DATE', y='ARR_DELAY_NEW', data=df_clean.iloc[:445827], color="blue", order=order,
                estimator=np.sum)
    plt.xticks(rotation=90)
    plt.title("Flight Date Vs Average Flight Arrival Delay in Minutes")
    plt.xlabel('Flight Date')
    plt.ylabel('Average Flight Arrival Delay in Minutes')
    plt.tight_layout()
    plt.show()

    # common.save_fig('Flight Date Vs Average Flight Arrival Delay in Minutes', file_path)

def explore_carrier_vs_delay(df_clean):
    sns.set_style('whitegrid')
    carrier_order = np.unique(list(df_clean['UNIQUE_CARRIER'].iloc[:445827]))
    sns.barplot(x='UNIQUE_CARRIER', y='ARR_DELAY_NEW', data=df_clean.iloc[:445827], color="blue", order=carrier_order)
    plt.title("Flight Carrier Vs Average Flight Arrival Delay in Minutes")
    plt.xlabel('Flight Carrier ')
    plt.ylabel('Average Flight Arrival Delay in Minutes')
    plt.tight_layout()
    plt.show()

    # common.save_fig('Flight Carrier Vs Average Flight Arrival Delay in Minutes', file_path)

    flight_carrier_grouped = df_clean.iloc[:445827].groupby('UNIQUE_CARRIER').mean()

    sns.set_style('whitegrid')
    sns.barplot(x=flight_carrier_grouped.index, y="ARR_DEL15", data=flight_carrier_grouped, color='blue')
    plt.title("Flight Carrier Vs Average Flight Arrival Delay")
    plt.xlabel('Flight Carrier ')
    plt.ylabel('Average Flight Arrival Delay')
    plt.tight_layout()
    plt.show()

    # common.save_fig('Flight Carrier Vs Average Flight Arrival Delay', file_path)

def explore_time_vs_delay(df_clean):

    Month_grouped1 = df_clean.groupby('MONTH')["ARR_DEL15"].sum()
    Month_grouped2 = df_clean.groupby('MONTH')["ARR_DEL15"].count()
    Month_grouped = pd.concat([Month_grouped1, Month_grouped2], axis=1, keys=["sum", "count"])
    Month_grouped["Average number of Arrival delays"] = Month_grouped["sum"] / Month_grouped["count"]

    sns.set_style('whitegrid')
    sns.barplot(x=Month_grouped.index, y='Average number of Arrival delays', data=Month_grouped, color='blue')
    plt.xlabel("Weekly distribution")
    plt.ylabel("Average number of Flight arrival delays")
    plt.title("Weekly distribution of a month Vs Average number of Flight arrival Delay")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Weekly distribution of a month Vs Average number of Flight arrival Delay', file_path)

    week_grouped1 = df_clean.groupby('WEEK')["ARR_DEL15"].sum()
    week_grouped2 = df_clean.groupby('WEEK')["ARR_DEL15"].count()
    week_grouped = pd.concat([week_grouped1, week_grouped2], axis=1, keys=["sum", "count"])
    week_grouped["Probability of Flight Arrival Delay"] = week_grouped["sum"] / week_grouped["count"]

    sns.set_style('whitegrid')
    sns.barplot(x=week_grouped.index, y='Probability of Flight Arrival Delay', data=week_grouped, color='blue')
    plt.xlabel("Part of a Week")
    plt.ylabel("Average Flight Arrival Delay")
    plt.title("Part of a Week Vs Average Flight Arrival Delay")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Part of a Week Vs Average Flight Arrival Delay', file_path)


def explore_origin_vs_delay(df_clean):

    airport_grouped1 = df_clean.groupby('ORIGIN_STATE_ABR')["ARR_DEL15"].sum()
    airport_grouped2 = df_clean.groupby('ORIGIN_STATE_ABR')["ARR_DEL15"].count()
    airport_grouped = pd.concat([airport_grouped1, airport_grouped2], axis=1, keys=["sum", "count"])
    airport_grouped["Probability of Flight Arrival Delay"] = airport_grouped["sum"] / airport_grouped["count"]
    airport_grouped.sort_values(by="Probability of Flight Arrival Delay", ascending=False, inplace=True)

    plt.figure(figsize=(8, 4))
    sns.set_style('whitegrid')
    sns.barplot(x=airport_grouped.index[:20], y="Probability of Flight Arrival Delay", data=airport_grouped[:20],
                color='blue')
    plt.xlabel("Origin State Airport")
    plt.ylabel("Average Flight Arrival Delay")
    plt.title("Origin State Airport Vs Average Flight Arrival Delay")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Origin State Airport Vs Average Flight Arrival Delay', file_path)

    airport_grouped3 = df_clean.groupby('DEST_STATE_ABR')["ARR_DEL15"].sum()
    airport_grouped4 = df_clean.groupby('DEST_STATE_ABR')["ARR_DEL15"].count()
    airport_grouped_dest = pd.concat([airport_grouped3, airport_grouped4], axis=1, keys=["sum", "count"])
    airport_grouped_dest["Probability of Flight Arrival Delay"] = airport_grouped_dest["sum"] / airport_grouped_dest[
        "count"]
    airport_grouped_dest.sort_values(by="Probability of Flight Arrival Delay", ascending=False, inplace=True)

    plt.figure(figsize=(8, 4))
    sns.set_style('whitegrid')
    sns.barplot(x=airport_grouped_dest.index[:20], y='Probability of Flight Arrival Delay',
                data=airport_grouped_dest[:20], color='blue')
    plt.xlabel("Destination State Airport")
    plt.ylabel("Average Flight Arrival Delay")
    plt.title("Destination state Airport Vs Average Flight Arrival Delay")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Destination state Airport Vs Average Flight Arrival Delay', file_path)

def explore_fligh_route_vs_delay(df_clean):

    flightroute = df_clean.groupby('Flight_route').sum()
    flightroute.sort_values(by="ARR_DEL15", axis=0, ascending=False, inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set_style('whitegrid')
    fig = sns.barplot(x=flightroute.index[:10], y="ARR_DEL15", data=flightroute[:10], color='blue')
    fig.set(xlabel='Flight Routes', ylabel='Average Flight Arrival Delay')
    plt.title("Flight routes Vs Average Flight Arrival Delay")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Flight routes Vs Average Flight Arrival Delay', file_path)

def explore_time_of_day_vs_delay(df_clean):

    arrival_time_grouped = df_clean.groupby('ARRIVAL_TIME').mean()
    departure_time_grouped = df_clean.groupby('Departure_Time').mean()

    sns.set_style('whitegrid')
    sns.barplot(x=arrival_time_grouped.index, y="ARR_DEL15", data=arrival_time_grouped, color='blue')
    plt.title("Arrival time Vs Average Flight Arrival Delay")
    plt.ylabel("Average Flight Arrival Delay")
    plt.xlabel("Time of Day")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Arrival time Vs Average Flight Arrival Delay', file_path)

    sns.set_style('whitegrid')
    sns.barplot(x=departure_time_grouped.index, y="ARR_DEL15", data=departure_time_grouped, color='blue')
    plt.title("Departure time Vs Average Flight Arrival Delay")
    plt.ylabel("Average Flight Arrival Delay")
    plt.xlabel("Time of Day")
    plt.tight_layout()
    plt.show()

    # common.save_fig('Departure time Vs Average Flight Arrival Delay', file_path)

