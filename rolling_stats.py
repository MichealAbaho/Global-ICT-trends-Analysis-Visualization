import pandas as plib
import numpy as num
import io
import matplotlib.pyplot as plt
from math import *
from matplotlib import style

style.use('ggplot')

def stats(file):

    fig = plt.figure()
    mv_average = []
    mv_std = []
    
    '''plotting the total number of subscriptions
    mobile, internet, fixbroad band, fixed telepjone per infrastructure'''
    readStats = plib.read_csv(file, encoding='latin1')
    years = readStats['Years'].tolist()
    
    readStats_List = (num.array(readStats).tolist())

    subscriptionType = ["Fixed\nTelephone", "Fixed\nBroadband", "Mobile\nCellular"]
    total_subscriptions = []

    for subtype in readStats:
        if((subtype != "Years") and (subtype != "indInternet_subscriptions")):
            total_subscriptions.append((num.nansum(readStats[subtype]))/1000000000)
    
    print (subscriptionType, '\n',total_subscriptions)

    x = [i for i in range(3)]
    font = {
        'color':  'black',
        'size': 13,
        'weight': 'normal'
        }

    plt.bar(x, total_subscriptions, color='g', align='center')
    plt.xticks(x, subscriptionType)
    plt.tick_params(axis='x', length=5, top='off', pad=-2)
    plt.tick_params(axis='y', length=5, right='off', colors='#f06215')
    plt.xlabel('Types of subscriptions', fontdict=font)
    plt.ylabel('Total subscriptions (in billions)', fontdict=font )
    plt.title('Subscription by Infrastructure Type')
    plt.show()


    '''plotting the average subscriptions as well as standard deviation of the subscriptions per year'''
    for i in readStats_List:
        moving_avergae = round(num.mean(i[1:4]))
        moving_sd = num.std(i[1:4])
        print (moving_sd/1000000)
        mv_std.append(moving_sd/1000000)
        mv_average.append(moving_avergae/1000000)
   
        
    change_in_subscription = plt.subplot2grid((6,1), (0,0), colspan =1, rowspan=4)
    change_in_subscription.plot(years, mv_average, c='darkred')
    change_in_subscription.tick_params(axis='x', length=5, top='off', colors='#f06215')
    change_in_subscription.tick_params(axis='y', length=5, right='off', colors='#f06215' )
    change_in_subscription.set_title('Changing average number of ICT Infrastructure \n subscriptions over the years')
    labels = [item.get_text() for item in change_in_subscription.get_xticklabels()]
    empty_string_labels = ['']*len(labels)
    change_in_subscription.set_xticklabels(empty_string_labels)
    plt.ylabel('# Average subscriptions in millions', fontdict=font)

    sd_in_subscriptions = plt.subplot2grid((6,1), (4,0), colspan=1, rowspan=2)
    sd_in_subscriptions.plot(years, mv_std, c='darkred')
    sd_in_subscriptions.tick_params(axis='y', length=5, right='off', colors='#f06215' )
    sd_in_subscriptions.tick_params(axis='x', length=5, top='off', pad=-2, colors='#f06215')
    sd_in_subscriptions.set_title('Chaning standard deviation of ICT Infrastructure \n  subscriptions over the years')
    sd_in_subscriptions.set_xticks(years)
    plt.ylabel('SD in millions', fontdict=font)
    plt.xticks(rotation=45)

  
    plt.xlabel('Years', fontdict=font)

    fig.subplots_adjust(hspace= 2, wspace=5)
    plt.show()

        
stats('../generated csv files/year_summary.csv')






















        