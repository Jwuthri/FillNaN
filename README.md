# FillNaN
Fill NaN using clustering approach


# How to use it ?
fn = FillNaN(filepath)
df_filled = fn.fill()

# Results ?

Real Data:
| Index   |      Data      |
|----------|:-------------:|
| 0 | 165349.20 | 
| 1 | 162597.70 | 
| 2 | 153441.51 | 
| 3 | 144372.41 | 
| 4 | 142107.34 | 
| 5 | 131876.90 | 
| 6 | 134615.46 | 
| 7 | 130298.13 | 
| 8 | 120542.52 | 
| 9 | 123334.88 | 



Filling NaN thanks to a KNN approach, we get a score of:
0.973
Filling NaN thanks to a mean approach, we get a score of:
0.847
