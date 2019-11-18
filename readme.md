t-test exploration
===
# introduction
this is a test to check a data set's appropriateness for hypothesis testing via student's t-test. the provided data contain three cases of paired sets of timing measurements. the t-test comparison is to check whether both timing sets *have the same mean*.  it is known that the timing measurements have a skewed, long-tailed (non-gaussian) distribution. however, it is also known that even for strongly non-gaussian distributions their sample means are gaussian in the limit that sample approaches infinity. 

# criteria
the student's t-test is an appropriate test to verify whether two values are taken from the same distribution under two main assumptions: 

- the values being compared are both (all) drawn from a gaussian distribution.
- the values being compared are drawn from a distribution of of equal variances.

# method
for each case, sample each set of timing measurements. for each sample, compute the mean. collect the means of the samples and compute their median, variance, standard deviation. plot a histogram of means, draw their median, and median +/- standard deviation. gauge skew ness and compare deviations. 

# results
the means of timing measurements are, by eye, close to having a gaussian distribution, but the variances are not the same across a pair. we conclude that instead of student's t-test, the [welch's test](https://en.wikipedia.org/wiki/Welch's_t-test) would be appropriate.
