import pandas as pd 
import numpy as np 
import os 


def load_data(folder_path):
    ## info for each sheet
    road_name = []
    direction = []
    station_no = []
    day = []
    date = []
    ## main data
    HRLY_Vol = []
    peak_hour = []
    
    folder_files = os.listdir(folder_path)
    
    for file in folder_files:
        try:
            data = pd.read_excel(folder_path + "/" + file)
            road_name.append(data.iloc[2,[0,3]][1])
            direction.append(data.iloc[3,[0,3]][1])
            station_no.append(data.iloc[4,[0,3]][1])
            day.append(list(data.iloc[[5,40,75],[0,3]].iloc[:,1]))
            date.append(data.iloc[[5,40,75],14])
            
            HRLY_Vol.append(data.iloc[[9,44,79],:].iloc[:,1:])
            peak_hour.append(data.iloc[[16,17,18,51,52,53,86,87,88],[1,3,6]])
    
        except ValueError:
            print("Can not read "+file)
            
    new_data  = pd.DataFrame({"Road Name": road_name, "Direction":direction,"Station No":station_no, "Day":day,"Date":date,"Houlry Volume":HRLY_Vol,"Peak Hour":peak_hour})
    new_data.to_csv("new_data/"+folder_path[13:]+"_extracted_data.csv")
            
    return new_data

def extract_info(new_data):
    hourly_volume1=[]
    hourly_volume2 =[]
    hourly_volume3 = []

    road_name = []
    direction = []

    dt1 = str(new_data["Date"].iloc[0].iloc[0])
    date1 = dt1[0:10]

    dt2 = str(new_data["Date"].iloc[0].iloc[1])
    date2 = dt2[0:10]

    dt3 = str(new_data["Date"].iloc[0].iloc[2])
    date3 = dt3[0:10]

    day1 = new_data["Day"].iloc[0][0]
    day2 = new_data["Day"].iloc[0][1]
    day3 = new_data["Day"].iloc[0][2]

    for i in range(len(new_data)):
        hv1 = new_data["Houlry Volume"].iloc[i].iloc[0].to_numpy()
        hourly_volume1.append(hv1[0:24])
        
        hv2 = new_data["Houlry Volume"].iloc[i].iloc[1].to_numpy()
        hourly_volume2.append(hv2[0:24])
        
        hv3 = new_data["Houlry Volume"].iloc[i].iloc[2].to_numpy()
        hourly_volume3.append(hv3[0:24])
        
        road_name.append(new_data["Road Name"].iloc[i])
        direction.append(new_data["Direction"].iloc[i])

    
    return hourly_volume1,date1,day1,hourly_volume2,date2,day2,hourly_volume3,date3,day3,road_name,direction

def peak_hours(new_data):
    wed_peakHours = []
    thurs_peakHours = []
    fri_peakHours = []
    
    x_wed = []
    y_wed = []

    x_thurs = []
    y_thurs = []

    x_fri = []
    y_fri = []

    for i in range(len(new_data)):
        wed_peakHours.append(new_data["Peak Hour"].iloc[i].iloc[0:3].to_numpy())
        thurs_peakHours.append(new_data["Peak Hour"].iloc[i].iloc[3:6].to_numpy())
        fri_peakHours.append(new_data["Peak Hour"].iloc[i].iloc[6:9].to_numpy())
    
    for ph in wed_peakHours:    
        for info in ph:
            x_wed.append(str(info[0])+" "+info[1])
            y_wed.append(info[2])
            
    for ph2 in thurs_peakHours:
        for info2 in ph2:
            x_thurs.append(str(info2[0])+" "+info2[1])
            y_thurs.append(info2[2])
            
    for ph3 in fri_peakHours:
        for info3 in ph3:
            x_fri.append(str(info3[0])+" "+info3[1])
            y_fri.append(info3[2])
    
    return x_wed, y_wed, x_thurs, y_thurs, x_fri,y_fri