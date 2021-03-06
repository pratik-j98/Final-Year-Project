import xlsxwriter
import random
workbook = xlsxwriter.Workbook('soildatasettrain.xlsx') 	#create a workbook
worksheet = workbook.add_worksheet()		   		#Add a worksheet

#Columnhead Name written in worksheet
worksheet.write('A1','PH')
worksheet.write('B1','Soil_moisture')
worksheet.write('C1','Soil_type')
worksheet.write('D1','Temperature')
worksheet.write('E1','Flowers')


#Details about roses
row=1
for i in range(0,500):
	worksheet.write(row,0,round(random.uniform(5.5,7),2))
	worksheet.write(row,1,random.randint(50,75))
	worksheet.write(row,2,"Loamy")
	worksheet.write(row,3,random.randint(18,25))
	worksheet.write(row,4,"Rose")
	row=row+1

#Details about Lilies
row=501
for i in range(0,500):
	worksheet.write(row,0,round(random.uniform(5.5,6.5),2))
	worksheet.write(row,1,random.randint(21,40))
	worksheet.write(row,2,"Sandy Loamy")
	worksheet.write(row,3,random.randint(20,30))
	worksheet.write(row,4,"Lilies")
	row=row+1

#Details about Cactus
row=1001
for i in range(0,500):
	worksheet.write(row,0,round(random.uniform(5,6.5),2))
	worksheet.write(row,1,random.randint(0,20))
	worksheet.write(row,2,"Dry")
	worksheet.write(row,3,random.randint(10,15))
	worksheet.write(row,4,"Cactus")
	row=row+1

#Details about Hibiscus
row=1501
a=["Loamy","Sandy Loamy"]
for i in range(0,500):
	worksheet.write(row,0,round(random.uniform(6.5,6.8),2))
	worksheet.write(row,1,random.randint(45,60))
	worksheet.write(row,2,random.choice(a))
	worksheet.write(row,3,random.randint(15,30))
	worksheet.write(row,4,"Hibiscus")
	row=row+1
workbook.close()
