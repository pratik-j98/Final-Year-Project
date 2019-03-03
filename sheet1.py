import xlsxwriter
import random
workbook = xlsxwriter.Workbook('soildatasettest.xlsx') 	
worksheet = workbook.add_worksheet()

#Columnhead Name written in worksheet
worksheet.write('A1','PH')
worksheet.write('B1','Soil_moisture')
worksheet.write('C1','Soil_type')
worksheet.write('D1','Temperature')
worksheet.write('E1','Fertilizer')

a=["Loamy","Sandy Loamy","Dry"]
b=["10-10-10","10-12-10","5-10-10","9-3-13","10","4-12","12-4-18"]
c=["Rose","Lilies","Cactus","Hibiscus"]

row=1
for i in range(0,100):
	worksheet.write(row,0,round(random.uniform(5.5,7),2))
	worksheet.write(row,1,random.randint(0,75))
	worksheet.write(row,2,random.choice(a))
	worksheet.write(row,3,random.randint(10,25))
	worksheet.write(row,4,random.choice(b))
	row=row+1

workbook.close()





