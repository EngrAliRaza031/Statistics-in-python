# Statistics-in-python
Mean, Median, Mode, Variance and Standard Deviation for grouped and ungrouped data using python

 
**Mean,Median and Mode for Grouped data:**
Class Boundary= lower limit - 0.5 and upper limit + 0.5
Cumulative frequency(c.f): adding each frequency from a frequency table to the sum of its previous frequencies.
X=(lower class limit + Upper class limit)/2
**Mean**= (∑fx)/(∑x)      Hint:(sum of fx / sum of f)
**Median**=  L+ ((N/2-F)/f)*h   
where:
	L is the lower-class boundary of the median class
	F is the cumulative frequency of class before median class
	f is the frequency of the median class
	N is the total number of the frequency
	h is the width of the median class(upper class boundary- lower class boundary)
  
**Mode:**
 
Where:
	L is the lower-class boundary of the modal group
	fm-1 is the frequency of the group before the modal group
	fm is the frequency of the modal group
	fm+1 is the frequency of the group after the modal group
	w is the group width
**Variance:**
Variance is calculated in five steps. First mean is calculated, then we calculate deviations from the mean, and thirdly the deviations are squared, fourthly the squared deviations are summed up and finally this sum is divided by number of items for which the variance is being calculated. Thus variance= Σ(xi-x-)/n. Where xi = ith. Number, x- = mean and n = number of items.
**For un group data:-**
Variance=(∑(xi-x ̅ )^2)/n
**For group data:-**
Variance=(∑f(xi-x ̅ )^2)/n
**Difference between population and sample variance:**
Population variance refers to the value of variance that is calculated from population data, and sample variance is the variance calculated from sample data. Due to this value of denominator in the formula for variance in case of sample data is ‘n-1’, and it is ‘n’ for population data. As a result both variance and standard deviation derived from sample data are more than those found out from population data.
**For sample data:**

Un grouped data:
Variance=(∑(xi-x ̅ )^2)/(n-1)

Group data:
Variance=(∑f(xi-x ̅ )^2)/(n-1)

**For population:**

Un grouped data:
Variance=(∑(xi-x ̅ )^2)/n

Group data:
Variance=(∑f(xi-x ̅ )^2)/n

**Standard Deviation:**

**For sample data:**

Un group data
S.D=sqrt((∑(xi-x ̅ )^2)/(n-1))
Group data:
S.D=sqrt((∑f(xi-x ̅ )^2)/(n-1))

**For population:**

Un group data
S.D=sqrt((∑(xi-x ̅ )^2)/n)

Group data:
S.D=sqrt((∑f(xi-x ̅ )^2)/n)

