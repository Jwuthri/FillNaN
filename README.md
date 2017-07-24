# FillNaN
Fill NaN using clustering approach


# How to use it ?
fn = FillNaN(filepath)
df_filled = fn.fill()

# Results ?

Real Data:
0    165349.20
1    162597.70
2    153441.51
3    144372.41
4    142107.34
5    131876.90
6    134615.46
7    130298.13
8    120542.52
9    123334.88

Missing Values:
0          NaN
1    162597.70
2    153441.51
3    144372.41
4          NaN
5    131876.90
6          NaN
7    130298.13
8    120542.52
9    123334.88

Filled Mean:
0     73419.698372
1    162597.700000
2    153441.510000
3    144372.410000
4     73419.698372
5    131876.900000
6     73419.698372
7    130298.130000
8    120542.520000
9    123334.880000

Filled Cluster:
0    149305.370000
1    162597.700000
2    153441.510000
3    144372.410000
4    149305.370000
5    131876.900000
6    107403.635714
7    130298.130000
8    120542.520000
9    123334.880000

Filling NaN thanks to a KNN approach, we get a score of:
0.973
Filling NaN thanks to a mean approach, we get a score of:
0.847
