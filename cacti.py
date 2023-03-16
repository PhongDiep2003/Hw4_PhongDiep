# fix the code to pass the test case where all subarray has length of 1 or 2


# check empty array [] and [[]]



def cacti_number(plantation):
# if empty array [] and [[]]
    if (len(plantation) == 0):
        return 0
    if (len(plantation[0]) == 0):
        return 0
    
# if array has blocks and plots
    availablePlots = 0
    blocks = len(plantation)
    plots = len(plantation[0])
    
    for i in range(blocks):
        for j in range(plots):
            if (plantation[i][j] == 0):
                plantation[i][j] = "plant"
                # check horizontal adjacency
                for k in range(max(0, j - 1), min(plots, j + 2)):
                    # only check adjacency plots. This if statement prevents checking the current plot. 
                    if (k != j):
                        if (plantation[i][k] == 1 or plantation[i][k] == 'plant'):
                            plantation[i][j] = "can't plant"
                
                # check vertical adjacency
                for k in range(max(0, i - 1), min(blocks, i + 2)):
                    if (k != i):
                        if (plantation[k][j] == 1 or plantation[k][j] == 'plant'):
                            plantation[i][j] = "can't plant"

    # count all the available plots
    for i in range(blocks):
        for j in range(plots):
            if (plantation[i][j] == "plant"):
                availablePlots += 1
    
    return availablePlots
            

print(cacti_number([[]]))
