# module 2

## area plot
display magnitude and proportion of multiple variables   
is based on the line plot   
must be sort by Desc   
```
dataframe_sort.plot(kind='area')
```

## histograms
represent the frequency distrbution of a dataset   
must be sort by bin edges   
```
dataframe_sort.plot(kind='hist')
```

## Bar chart
it compares the values of a variable   
```
dataframe_sort.plot(kind='bar')
```

## Pie chart
a circular statistical graphic, divided into segments   
```
dataframe_sort.plot(kind='pie')
```

## Box plot
```
dataframe_sort.plot(kind='box')
```

## Scatter plot
Display values pertaining to two variables
determines the correlation between the two variables
```
dataframe_sort.plot(kind='scatter', x=, y=)
```

## Treemaps
displays hierarchical data ising nested rectangles
```
import plotly.express as px
[...]
px.treemap(dataframe_sort,
            path=['Category','Subcategory'],
            values='Value',
            title='Example')
            
```

## Pivot Charts
dynamically summarize and explore large dataset revealing insights and trands.
```
pivot_table=dataframe_sort.pivot_tables(values='ValuesColumn', index='RowIndewColumn', columns='ColumnsIndexColumn', aggfunc='sum')
pivot_table.plot(kind='bar')
```

## Cheat sheet
| Plot Type |Description |Pandas Function |Example |Visual |
| --- |--- |--- |--- |--- |
|Line Plot|	Shows trends and changes over time|	```DataFrame.plot.line()``` ```DataFrame.plot(kind = ‘line’)``` |	```df.plot(x=’year’, y=’sales’, kind=’line’)```| ![Line Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/line_plot.png)	|
|Area Plot|	Displays data series as filled areas, showing the relationship between them|	```DataFrame.plot.area()``` ```DataFrame.plot(kind = ‘area’)```| ```df.plot(kind='area')```|![Area Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/area_plot.png)	|
|Histogram|	Displays bars representing the data count in each interval/bin|	```Series.plot.hist()``` ```Series.plot(kind = ‘hist’, bins = n)``` |	```s.plot(kind='hist', bins=10)``` ```df[‘age’].plot(kind='hist', bins=10)```|![Histogram](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/histogram.png)	|
|Bar Chart|	Displays data using rectangular bars|	```DataFrame.plot.bar()``` ```DataFrame.plot(kind = ‘bar’)``` |	```df.plot(kind='bar')```	| ![Bar Chart](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/bar_chart.png)|
|Pie Chart|	Displays data as a circular plot divided into slices, representing proportions or percentages of a whole|	```Series.plot.pie() Series.plot(kind = ‘pie’)``` ```DataFrame.plot.pie(y, labels)``` ```DataFrame.plot(kind = ‘pie’)```|	```s.plot kind='pie’,autopct='%1.1f%%')``` ```df.plot(x='Category',y='Percentage',kind='pie')```| ![Pie Chart](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/pie_chart.png)|	
|Box Plot|	Displays the distribution of a dataset along with key statistical measures|	```DataFrame.plot.box()``` ```DataFrame.plot(kind = ‘box’)```|	```df_can.plot(kind='box')```	| ![Box Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/box_plot.png)|
|Scatter Plot|	Uses Cartesian coordinates to display values for two variables|	```DataFrame.plot.scatter()``` ```DataFrame.plot(x, y, kind = ‘scatter’)```|```df.plot(x='Height', y='Weight', kind='scatter')```|![Scatter Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/scatter.png)|
   
| Plot Type| Description | Matplotlib Function | Example | Visual |
| --- | --- | --- | --- | ---|
|Line Plot|	Shows trends and changes over time|	```plt.plot()```|	```plt.plot(x, y, color='red', linewidth=2)```	|![Line Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/line.png)|
|Area Plot|	Display data series as filled areas|	```plt.fill_between()```|	```plt.fill_between(x, y1, y2, color='blue', alpha=0.5)```	|![Area Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/area_plot.png)|
|Histogram|	Displays bars representing the data count in each interval/bin|	```plt.hist()```|	```plt.hist(data, bins=10, color='orange', edgecolor='black')```	|![Histogram](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/hist.png)|
|Bar Chart|	Displays data using rectangular bars|	```plt.bar()```|	```plt.bar(x, height, color='green', width=0.5)```	|![Bar Chart](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/bar.png)|
|Pie Chart|	Displays data as a circular plot divided into slices, representing proportions or percentages of a whole|	```plt.pie()```|	```plt.pie(sizes, labels=labels, colors=colors, explode=explode)```	|![Pie Chart](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/pie_chart.png)|
|Box Plot|	Displays the distribution of a dataset along with key statistical measures|	```plt.boxplot()```|	```plt.boxplot(data, notch=True)```	|![Box Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/box.png)|
|Scatter Plot|	Uses Cartesian coordinates to display values for two variables|	```plt.scatter()```|	```plt.scatter(x, y, color='purple', marker='o', s=50)```	|![Scatter Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/scatter_without_out.png)|
|Subplotting|	Creating multiple plots on one figure|	```plt.subplots()```|	```fig, axes = plt.subplots(nrows=2, ncols=2)```	|![Subplotting](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/Line_Scatter_shareY.png)|
|Customization|	Customizing plot: adding labels, title, legend, grid | Various customization|	```plt.title('Title')``` ```plt.xlabel('X Label')``` ```plt.ylabel('Y Label')``` ```plt.legend()``` ```plt.grid(True)```	|![Customization Plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/customized.png)|