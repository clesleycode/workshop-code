import pandas as pd

class Bayes(object):
  
	def __init__(self, dir): 
		self.f1 = pd.read_csv(dir) # creates initial dataframe

	def get_df1(self):
		df1 = self.f1.groupby('Play').count() 
		df1['Likelihood'] = df1['Weather']/len(self.f1) # adds likelihood column by dividing counts by total length
		return(df1)

	def get_df2(self):
		df2 = self.f1.groupby('Weather').count() 
		df2['Likelihood'] = df2['Play']/len(self.f1)
		return(df2)

	def get_ps(self):
		df2 = self.get_df2()
		ps = df2['Likelihood']['Sunny'] # adds likelihood column by dividing counts by total length
		return(ps)

	def get_py(self):
		df1 = self.get_df1()
		py = df1['Likelihood']['Yes']
		return(py)

	def get_psy(self):
		df = self.f1.groupby(['Weather','Play']).size()
		df1 = self.get_df1()
		psy = df['Sunny']['Yes']/df1['Weather']['Yes']
		return(psy)

  # returns bayes prob
	def final_prob(self, psy, py, ps):
		p = (psy*py)/ps
		return(p)
