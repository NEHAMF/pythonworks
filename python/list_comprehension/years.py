# 1800-2024
years=[n for n in range(1800,2025)]
print(years)

cen_years=[n for n in years if n %100==0]
print(cen_years)

noncen_years=[n for n in years if n %100!=0]
print(noncen_years)