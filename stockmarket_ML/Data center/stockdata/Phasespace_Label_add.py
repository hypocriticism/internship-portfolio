def Dimension_append_Trade_movingaverage(DD, T, j):
    ##
    DD.append(math.log(T[j] + 1) - math.log(movingaverage(T, j + 95, 95) + 1))
    DD.append(math.log(T[j] + 1) - math.log(movingaverage(T, j + 60, 60) + 1))
    DD.append(math.log(T[j] + 1) - math.log(movingaverage(T, j + 30, 30) + 1))
    DD.append(math.log(T[j] + 1) - math.log(movingaverage(T, j + 10, 10) + 1))
    DD.append(math.log(T[j] + 1) - math.log(movingaverage(T, j + 5, 5) + 1))

    DD.append(math.log(T[j + 1] + 1) - math.log(movingaverage(T, j + 96, 95) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(movingaverage(T, j + 61, 60) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(movingaverage(T, j + 31, 30) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(movingaverage(T, j + 11, 10) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(movingaverage(T, j + 6, 5) + 1))

    DD.append(math.log(T[j + 2] + 1) - math.log(movingaverage(T, j + 97, 95) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(movingaverage(T, j + 62, 60) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(movingaverage(T, j + 32, 30) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(movingaverage(T, j + 12, 10) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(movingaverage(T, j + 7, 5) + 1))

    DD.append(math.log(T[j + 3] + 1) - math.log(movingaverage(T, j + 98, 95) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(movingaverage(T, j + 63, 60) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(movingaverage(T, j + 33, 30) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(movingaverage(T, j + 13, 10) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(movingaverage(T, j + 8, 5) + 1))

    DD.append(math.log(T[j + 4] + 1) - math.log(movingaverage(T, j + 99, 95) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(movingaverage(T, j + 64, 60) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(movingaverage(T, j + 34, 30) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(movingaverage(T, j + 14, 10) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(movingaverage(T, j + 9, 5) + 1))

    DD.append(math.log(T[j + 5] + 1) - math.log(movingaverage(T, j + 100, 95) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(movingaverage(T, j + 65, 60) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(movingaverage(T, j + 35, 30) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(movingaverage(T, j + 15, 10) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(movingaverage(T, j + 10, 5) + 1))

def Dimension_append_Trade_Local_Maximum(DD, T, j):
    ##
    DD.append(math.log(T[j] + 1) - math.log(Local_Maximum(T, j + 95, 95) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Maximum(T, j + 60, 60) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Maximum(T, j + 30, 30) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Maximum(T, j + 10, 10) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Maximum(T, j + 5, 5) + 1))

    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Maximum(T, j + 96, 95) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Maximum(T, j + 61, 60) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Maximum(T, j + 31, 30) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Maximum(T, j + 11, 10) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Maximum(T, j + 6, 5) + 1))

    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Maximum(T, j + 97, 95) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Maximum(T, j + 62, 60) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Maximum(T, j + 32, 30) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Maximum(T, j + 12, 10) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Maximum(T, j + 7, 5) + 1))

    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Maximum(T, j + 98, 95) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Maximum(T, j + 63, 60) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Maximum(T, j + 33, 30) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Maximum(T, j + 13, 10) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Maximum(T, j + 8, 5) + 1))

    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Maximum(T, j + 99, 95) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Maximum(T, j + 64, 60) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Maximum(T, j + 34, 30) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Maximum(T, j + 14, 10) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Maximum(T, j + 9, 5) + 1))

    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Maximum(T, j + 100, 95) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Maximum(T, j + 65, 60) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Maximum(T, j + 35, 30) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Maximum(T, j + 15, 10) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Maximum(T, j + 10, 5) + 1))

def Dimension_append_Trade_Local_Minimum(DD, T, j):
    ##
    DD.append(math.log(T[j] + 1) - math.log(Local_Minimum(T, j + 95, 95) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Minimum(T, j + 60, 60) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Minimum(T, j + 30, 30) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Minimum(T, j + 10, 10) + 1))
    DD.append(math.log(T[j] + 1) - math.log(Local_Minimum(T, j + 5, 5) + 1))

    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Minimum(T, j + 96, 95) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Minimum(T, j + 61, 60) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Minimum(T, j + 31, 30) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Minimum(T, j + 11, 10) + 1))
    DD.append(math.log(T[j + 1] + 1) - math.log(Local_Minimum(T, j + 6, 5) + 1))

    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Minimum(T, j + 97, 95) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Minimum(T, j + 62, 60) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Minimum(T, j + 32, 30) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Minimum(T, j + 12, 10) + 1))
    DD.append(math.log(T[j + 2] + 1) - math.log(Local_Minimum(T, j + 7, 5) + 1))

    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Minimum(T, j + 98, 95) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Minimum(T, j + 63, 60) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Minimum(T, j + 33, 30) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Minimum(T, j + 13, 10) + 1))
    DD.append(math.log(T[j + 3] + 1) - math.log(Local_Minimum(T, j + 8, 5) + 1))

    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Minimum(T, j + 99, 95) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Minimum(T, j + 64, 60) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Minimum(T, j + 34, 30) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Minimum(T, j + 14, 10) + 1))
    DD.append(math.log(T[j + 4] + 1) - math.log(Local_Minimum(T, j + 9, 5) + 1))

    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Minimum(T, j + 100, 95) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Minimum(T, j + 65, 60) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Minimum(T, j + 35, 30) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Minimum(T, j + 15, 10) + 1))
    DD.append(math.log(T[j + 5] + 1) - math.log(Local_Minimum(T, j + 10, 5) + 1))

def Dimension_append_movingaverage(DD, _T, T, j):
    ##
    DD.append(_T[j] / movingaverage(T, j + 95, 95))
    DD.append(_T[j] / movingaverage(T, j + 60, 60))
    DD.append(_T[j] / movingaverage(T, j + 30, 30))
    DD.append(_T[j] / movingaverage(T, j + 10, 10))
    DD.append(_T[j] / movingaverage(T, j + 5, 5))

    DD.append(_T[j + 1] / movingaverage(T, j + 96, 95))
    DD.append(_T[j + 1] / movingaverage(T, j + 61, 60))
    DD.append(_T[j + 1] / movingaverage(T, j + 31, 30))
    DD.append(_T[j + 1] / movingaverage(T, j + 11, 10))
    DD.append(_T[j + 1] / movingaverage(T, j + 6, 5))

    DD.append(_T[j + 2] / movingaverage(T, j + 97, 95))
    DD.append(_T[j + 2] / movingaverage(T, j + 62, 60))
    DD.append(_T[j + 2] / movingaverage(T, j + 32, 30))
    DD.append(_T[j + 2] / movingaverage(T, j + 12, 10))
    DD.append(_T[j + 2] / movingaverage(T, j + 7, 5))

    DD.append(_T[j + 3] / movingaverage(T, j + 98, 95))
    DD.append(_T[j + 3] / movingaverage(T, j + 63, 60))
    DD.append(_T[j + 3] / movingaverage(T, j + 33, 30))
    DD.append(_T[j + 3] / movingaverage(T, j + 13, 10))
    DD.append(_T[j + 3] / movingaverage(T, j + 8, 5))

    DD.append(_T[j + 4] / movingaverage(T, j + 99, 95))
    DD.append(_T[j + 4] / movingaverage(T, j + 64, 60))
    DD.append(_T[j + 4] / movingaverage(T, j + 34, 30))
    DD.append(_T[j + 4] / movingaverage(T, j + 14, 10))
    DD.append(_T[j + 4] / movingaverage(T, j + 9, 5))

    DD.append(_T[j + 5] / movingaverage(T, j + 100, 95))
    DD.append(_T[j + 5] / movingaverage(T, j + 65, 60))
    DD.append(_T[j + 5] / movingaverage(T, j + 35, 30))
    DD.append(_T[j + 5] / movingaverage(T, j + 15, 10))
    DD.append(_T[j + 5] / movingaverage(T, j + 10, 5))

def Dimension_append_Local_Maximum(DD, _T, T, j):
    ##
    DD.append(_T[j] / Local_Maximum(T, j + 95, 95))
    DD.append(_T[j] / Local_Maximum(T, j + 60, 60))
    DD.append(_T[j] / Local_Maximum(T, j + 30, 30))
    DD.append(_T[j] / Local_Maximum(T, j + 10, 10))
    DD.append(_T[j] / Local_Maximum(T, j + 5, 5))

    DD.append(_T[j + 1] / Local_Maximum(T, j + 96, 95))
    DD.append(_T[j + 1] / Local_Maximum(T, j + 61, 60))
    DD.append(_T[j + 1] / Local_Maximum(T, j + 31, 30))
    DD.append(_T[j + 1] / Local_Maximum(T, j + 11, 10))
    DD.append(_T[j + 1] / Local_Maximum(T, j + 6, 5))

    DD.append(_T[j + 2] / Local_Maximum(T, j + 97, 95))
    DD.append(_T[j + 2] / Local_Maximum(T, j + 62, 60))
    DD.append(_T[j + 2] / Local_Maximum(T, j + 32, 30))
    DD.append(_T[j + 2] / Local_Maximum(T, j + 12, 10))
    DD.append(_T[j + 2] / Local_Maximum(T, j + 7, 5))

    DD.append(_T[j + 3] / Local_Maximum(T, j + 98, 95))
    DD.append(_T[j + 3] / Local_Maximum(T, j + 63, 60))
    DD.append(_T[j + 3] / Local_Maximum(T, j + 33, 30))
    DD.append(_T[j + 3] / Local_Maximum(T, j + 13, 10))
    DD.append(_T[j + 3] / Local_Maximum(T, j + 8, 5))

    DD.append(_T[j + 4] / Local_Maximum(T, j + 99, 95))
    DD.append(_T[j + 4] / Local_Maximum(T, j + 64, 60))
    DD.append(_T[j + 4] / Local_Maximum(T, j + 34, 30))
    DD.append(_T[j + 4] / Local_Maximum(T, j + 14, 10))
    DD.append(_T[j + 4] / Local_Maximum(T, j + 9, 5))

    DD.append(_T[j + 5] / Local_Maximum(T, j + 100, 95))
    DD.append(_T[j + 5] / Local_Maximum(T, j + 65, 60))
    DD.append(_T[j + 5] / Local_Maximum(T, j + 35, 30))
    DD.append(_T[j + 5] / Local_Maximum(T, j + 15, 10))
    DD.append(_T[j + 5] / Local_Maximum(T, j + 10, 5))

def Dimension_append_Local_Minimum(DD, _T, T, j):
    ##
    DD.append(_T[j] / Local_Minimum(T, j + 95, 95))
    DD.append(_T[j] / Local_Minimum(T, j + 60, 60))
    DD.append(_T[j] / Local_Minimum(T, j + 30, 30))
    DD.append(_T[j] / Local_Minimum(T, j + 10, 10))
    DD.append(_T[j] / Local_Minimum(T, j + 5, 5))

    DD.append(_T[j + 1] / Local_Minimum(T, j + 96, 95))
    DD.append(_T[j + 1] / Local_Minimum(T, j + 61, 60))
    DD.append(_T[j + 1] / Local_Minimum(T, j + 31, 30))
    DD.append(_T[j + 1] / Local_Minimum(T, j + 11, 10))
    DD.append(_T[j + 1] / Local_Minimum(T, j + 6, 5))

    DD.append(_T[j + 2] / Local_Minimum(T, j + 97, 95))
    DD.append(_T[j + 2] / Local_Minimum(T, j + 62, 60))
    DD.append(_T[j + 2] / Local_Minimum(T, j + 32, 30))
    DD.append(_T[j + 2] / Local_Minimum(T, j + 12, 10))
    DD.append(_T[j + 2] / Local_Minimum(T, j + 7, 5))

    DD.append(_T[j + 3] / Local_Minimum(T, j + 98, 95))
    DD.append(_T[j + 3] / Local_Minimum(T, j + 63, 60))
    DD.append(_T[j + 3] / Local_Minimum(T, j + 33, 30))
    DD.append(_T[j + 3] / Local_Minimum(T, j + 13, 10))
    DD.append(_T[j + 3] / Local_Minimum(T, j + 8, 5))

    DD.append(_T[j + 4] / Local_Minimum(T, j + 99, 95))
    DD.append(_T[j + 4] / Local_Minimum(T, j + 64, 60))
    DD.append(_T[j + 4] / Local_Minimum(T, j + 34, 30))
    DD.append(_T[j + 4] / Local_Minimum(T, j + 14, 10))
    DD.append(_T[j + 4] / Local_Minimum(T, j + 9, 5))

    DD.append(_T[j + 5] / Local_Minimum(T, j + 100, 95))
    DD.append(_T[j + 5] / Local_Minimum(T, j + 65, 60))
    DD.append(_T[j + 5] / Local_Minimum(T, j + 35, 30))
    DD.append(_T[j + 5] / Local_Minimum(T, j + 15, 10))
    DD.append(_T[j + 5] / Local_Minimum(T, j + 10, 5))

def Dimension_append_Ratio(DD, _T, T, _j, j):
    DD.append(_T[_j] / T[j])
    DD.append(_T[_j] / T[j + 1])
    DD.append(_T[_j] / T[j + 2])
    DD.append(_T[_j] / T[j + 3])
    DD.append(_T[_j] / T[j + 4])
    DD.append(_T[_j] / T[j + 5])

def Dimension_append_Trade_Ratio(DD, T, _j, j):
    DD.append(math.log(T[_j] + 1) - math.log(T[j] + 1))
    DD.append(math.log(T[_j] + 1) - math.log(T[j + 1] + 1))
    DD.append(math.log(T[_j] + 1) - math.log(T[j + 2] + 1))
    DD.append(math.log(T[_j] + 1) - math.log(T[j + 3] + 1))
    DD.append(math.log(T[_j] + 1) - math.log(T[j + 4] + 1))
    DD.append(math.log(T[_j] + 1) - math.log(T[j + 5] + 1))
    
# Dimensions Begin
Dimension_append_Trade_movingaverage(DD, T, j)
Dimension_append_Trade_Local_Maximum(DD, T, j)
Dimension_append_Trade_Local_Minimum(DD, T, j)

Dimension_append_movingaverage(DD, P, P, j)
Dimension_append_movingaverage(DD, H, P, j)
Dimension_append_movingaverage(DD, L, P, j)
Dimension_append_movingaverage(DD, S, P, j)
        
Dimension_append_Local_Maximum(DD, P, H, j)
Dimension_append_Local_Minimum(DD, P, L, j)

Dimension_append_Trade_Ratio(DD, T, j, j)
Dimension_append_Trade_Ratio(DD, T, j + 1, j)
Dimension_append_Trade_Ratio(DD, T, j + 2, j)
Dimension_append_Trade_Ratio(DD, T, j + 3, j)
Dimension_append_Trade_Ratio(DD, T, j + 4, j)
Dimension_append_Trade_Ratio(DD, T, j + 5, j)

Dimension_append_Ratio(DD, P, P, j, j)
Dimension_append_Ratio(DD, P, P, j + 1, j)
Dimension_append_Ratio(DD, P, P, j + 2, j)
Dimension_append_Ratio(DD, P, P, j + 3, j)
Dimension_append_Ratio(DD, P, P, j + 4, j)
Dimension_append_Ratio(DD, P, P, j + 5, j)

Dimension_append_Ratio(DD, P, S, j, j)
Dimension_append_Ratio(DD, P, S, j + 1, j)
Dimension_append_Ratio(DD, P, S, j + 2, j)
Dimension_append_Ratio(DD, P, S, j + 3, j)
Dimension_append_Ratio(DD, P, S, j + 4, j)
Dimension_append_Ratio(DD, P, S, j + 5, j)
# Dimensions End
