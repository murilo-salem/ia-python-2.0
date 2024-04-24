import scipy.stats as stats

x1_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y1_values = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y2_values = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3_values = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y3_values = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

x4_values = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4_values = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]

slope, intercept, r_value, p_value, std_err = stats.linregress(x1_values, y1_values)

slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2_values, y2_values)

slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(x3_values, y3_values)

slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(x4_values, y4_values)

print(f"Coeficiente Angular (slope): {slope:.3f}")
print(f"Coeficiente de Correlação (r-value): {r_value:.3f}")

print(f"Coeficiente Angular (slope): {slope2:.3f}")
print(f"Coeficiente de Correlação (r-value): {r_value2:.3f}")

print(f"Coeficiente Angular (slope): {slope3:.3f}")
print(f"Coeficiente de Correlação (r-value): {r_value3:.3f}")

print(f"Coeficiente Angular (slope): {slope4:.3f}")
print(f"Coeficiente de Correlação (r-value): {r_value4:.3f}")
