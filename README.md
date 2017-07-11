# FillNaN
Fill NaN using clustering approach


# How to use it ?
fn = FillNaN(filepath)
df_filled = fn.fill()

# Results ?

| Index | Real Data | Missing Data | Filled Mean | Filled Cluster |
|----------|:-------------:|:-------------:|:-------------:|-------------:|
| 0 | 165349.20 | NaN | 73419.698372 | 149305.370000 | 
| 1 | 162597.70 | 162597.700000 | 162597.700000 | 162597.700000 | 
| 2 | 153441.51 | 153441.510000 | 153441.510000 | 153441.510000 | 
| 3 | 144372.41 | 144372.410000 | 144372.410000 | 144372.410000 |
| 4 | 142107.34 | NaN | 73419.698372 | 149305.370000 |
| 5 | 131876.90 | 131876.900000 | 131876.900000 | 131876.900000 |
| 6 | 134615.46 | NaN | 73419.698372 | 107403.635714 |
| 7 | 130298.13 | 130298.130000 | 130298.130000 | 130298.130000 |
| 8 | 120542.52 | 120542.520000 | 120542.520000 | 120542.520000 |
| 9 | 123334.88 | 123334.880000 | 123334.880000 | 123334.880000 |
