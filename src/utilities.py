def get_inlier_limits(series_of_observations):
    """
    computes the bounds of outlier obervations using tukey's method,
    i.e. 1.5 x iqr below q1 or above q3
    """
    series_of_observations = sorted(series_of_observations)
    Q1,Q3 = np.percentile(series_of_observations, [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range,upper_range

def check_whether_inlier(value, lower, upper):
    """checks whether input value is within bounds """
    return (value>=lower) & (value<=upper)

def sample_with_replacement(a_series, num_samples):
    return None

def drop_nulls(a_series):
    """returns the input series with all the null rows dropped"""
    return a_series[~ a_series.isna()]

def case_histogram(times, casename, idstr):
    """given a series of timing observations, plots their histogram and saves to disk"""
    median = np.median(times)
    plt.figure(figsize=(13,9))
    n, bins, patches = plt.hist(x=times, bins='auto', color='blue',
                                alpha=0.7, rwidth=0.85);
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('time [ms]')
    plt.ylabel('frequency')
    plt.title(casename+' '+idstr)
    # plt.text(23, 45, r'$\mu=, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(os.path.join(graph_folder,casename+'_'+idstr+'.png'))
#     plt.show()
    
def histogram_of_means(means, casename):
    """given a series of timing sample means, plots their histogram and saves to disk"""
    median = np.median(means)
    std    = np.std(means)

    verticals = [
        median - std,
        median,
        median + std
    ]

    title = casename\
        + ' means of samples.'\
        +' median: '+ str(round(median,0))\
        +' std:'+str(round(std,0))

    plt.figure(figsize=(15,9))
    
    n, bins, patches = plt.hist(x=means, bins='auto', color='red',
                                alpha=0.7, rwidth=0.85)
    
    plt.grid(axis='y', alpha=0.7)
    plt.xlabel('time [ms]')
    plt.ylabel('frequency')
    plt.title(title)

    for x_position in verticals:
        plt.axvline(x=x_position, color='gray', linestyle='--')

    plt.axvline(x=median, color='k', linestyle='-', lw=3)
    
#     plt.text(23, 45, r'$\mu=, b=3$')
    # Set a clean upper y-axis limit.
    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(os.path.join(graph_folder,casename+'_means.png'))
    plt.show()