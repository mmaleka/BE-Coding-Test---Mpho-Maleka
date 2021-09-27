import pandas as pd # Import pandas


def leagueSort(league_list):


    league_list_list = []
    league_teams = []
    for i in range(len(league_list)):
        x = league_list[i].split(",")
        x1 = x[0].rstrip().rsplit(' ', 1)
        x2 = x[1].rstrip().rsplit(' ', 1)

        # create a teams only list
        if x1[0].lstrip() not in league_teams:
            league_teams.append(x1[0])
        if x2[0].lstrip() not in league_teams:
            league_teams.append(x2[0])
        # create a list of teams and score
        league_list_list.append(x1+x2)

    league_teams_points = [0]*len(league_teams)
    # Create a zip object from two lists
    league_teamsbObj = zip(league_teams, league_teams_points)
    # Create a dictionary from zip object
    dictOfleague_teams = dict(league_teamsbObj)

    for p in range(len(league_list_list)):
        if league_list_list[p][1] > league_list_list[p][3]:
            # now update the dictOfleague_teams
            dictOfleague_teams.update({league_list_list[p][0]: dictOfleague_teams[league_list_list[p][0]]+3})

        elif league_list_list[p][1] < league_list_list[p][3]:
            # now update the dictOfleague_teams
            dictOfleague_teams.update({league_list_list[p][2]: dictOfleague_teams[league_list_list[p][2]]+3})


        elif league_list_list[p][1] == league_list_list[p][3]:
            # now update the dictOfleague_teams
            dictOfleague_teams.update({league_list_list[p][0]: dictOfleague_teams[league_list_list[p][0]]+1})
            dictOfleague_teams.update({league_list_list[p][2]: dictOfleague_teams[league_list_list[p][2]]+1})


    df_dictOfleague_teams = pd.DataFrame.from_dict(dictOfleague_teams, orient='index')
    df_dictOfleague_teams['Teams'] = df_dictOfleague_teams.index
    df_dictOfleague_teams = df_dictOfleague_teams.sort_values([0, 'Teams'], ascending=[False, True])
    # print("df_dictOfleague_teams: ", df_dictOfleague_teams)

    # initialise position 
    position = 1
    pointsName = " pt"
    for i in range(0, len(df_dictOfleague_teams), 1):
        if i == 0:
            if df_dictOfleague_teams.iloc[i, 0] > 1 or df_dictOfleague_teams.iloc[i, 0] < 1:
                pointsName = " pts"
            elif df_dictOfleague_teams.iloc[i, 0] == 1:
                pointsName = " pt"
            
            print(position, df_dictOfleague_teams.index[i] + ", ", str(
                df_dictOfleague_teams.iloc[i, 0]).lstrip() + pointsName)
            position = 2
                
        else:
            if df_dictOfleague_teams.iloc[i, 0] == df_dictOfleague_teams.iloc[i-1, 0]:
                if df_dictOfleague_teams.iloc[i, 0] > 1 or df_dictOfleague_teams.iloc[i, 0] < 1:
                    pointsName = " pts"
                elif df_dictOfleague_teams.iloc[i, 0] == 1:
                    pointsName = " pt"

                print(position, df_dictOfleague_teams.index[i].lstrip() + ", ", str(df_dictOfleague_teams.iloc[i-1, 0]) + pointsName)
            else:
                if df_dictOfleague_teams.iloc[i, 0] > 1 or df_dictOfleague_teams.iloc[i, 0] < 1:
                    pointsName = " pts"
                elif df_dictOfleague_teams.iloc[i, 0] == 1:
                    pointsName = " pt"
                position = i+1
                print(position, df_dictOfleague_teams.index[i].lstrip() + ", ", str(
                    df_dictOfleague_teams.iloc[i, 0]) + pointsName)
                

    return "pass"


    


if __name__ == '__main__':
    league_file = input("Enter file name without extension: ")
    print("league_file: ", league_file)
    league_file = open(league_file+".txt", "r")
    content_list = league_file.readlines()
    league_list = []
    for i in range(len(content_list)):
        league_list.append(content_list[i].strip('\n'))

    
    leagueSort(league_list)


    league_file.close()
