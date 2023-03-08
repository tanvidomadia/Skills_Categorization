import pandas

#reading the files in DataFrame(df)
df1 = pandas.read_csv("Results2.csv")
df2 = pandas.read_csv("datashop_result.csv")
#df2['Skill'] = df2['Skill'].astype(str)+'.'

#merging the df1 and df2 
df6 = df2.merge(df1, on='Skill', how='left')

#storing lists in df and converting df to csv
df6.to_csv("categories_skills.csv", index = False)

