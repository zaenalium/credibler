import pandas as pd
import ydata_profiling 

from toad import detect, quality

class StatDesc:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def report(self, minimal: bool = True):
        '''
        Generate a ProfileReport using ydata_profiling (minimal computation by default)

        Args:
            df: a pandas or spark.sql DataFrame
            minimal: minimal mode is a default configuration with minimal computation

        Returns:
            html report
        '''

        profile = ydata_profiling.ProfileReport(self.df, minimal = minimal)
        report = profile.to_html()
        return report

    def summary(self):
        '''
        get summary statistics of the dataframe
        '''
        report = detect(self.df)
        return report

    def predictive_quality(self, target='target', iv_only=False, **kwargs):
        '''
        get predictive quality of the features/variable to predict the target using iv, gini, entropy 
        '''
                
        report = quality(self.df, target, iv_only, **kwargs)
        return report
