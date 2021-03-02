
import csv


SODH = ["No high school diploma", "Unemployment", "Homelessness", "Lack of adequate food/water", "Poverty", "sexual abuse of child", "imprisonment", "veteran", "nonveteran"]
diseases = ['Depression', 'Hypertension', 'Coronary Heart Disease', 'Stroke', 'Heart Attack', 'Substance Use Disorder', 'Chronic Kidney Disease', 'PTSD', 'Obesity', 'Mental Illness', 'HIV+', 'Diabetes/Prediabetes', 'anemia', 'hypercholesterolemia', 'ADHD', 'Generalized anxiety disorder', 'Alcohol abuse/dependence', 'left ventricular hypertrophy', 'atrial fibrilation', 'frequent mental distress', 'traumatic brain injury', 'chlamydia', 'Gonhorrea', 'Hepatitis C', 'syphillis', 'cancer', 'asthma', 'cirrhosis', 'Schizophrenia', 'bipolar disorder', 'borderline personality disorder', 'psychosis', 'suicide attempt', 'tobacco substance use disorder', 'cannabis substance use disorder', 'sedatives substance use disorder', 'heroin substance use disorder', 'cocaine substance use disorder', 'cognitive impairment', 'gambling disorder', 'vision problems', 'chronic moderate to severe pain', 'arthritis', 'herpes', 'Latent tuberculosis', 'social isolation', 'malignant growth on skin', 'methicillin-risistent S. aureus', 'tinea pedis', 'pitted keratolysis of the feet', 'toenail onychomycosis', 'acne vulgaris', 'seborrheic dermatitis', 'Untreated caries', 'Mania', 'panic disorder', 'social phobia', 'specific phobia', 'nicotine dependence', 'conduct disorder', 'Intercranial hemmorhage', 'STI', 'fracture of spine, hands, and feet', 'insomnia', 'thrombotic thrombocytopenic purpura', 'fibromyalgia', 'CNS Tumor', 'infantile eczema', 'overactive bladder', 'pediatric hearing loss', 'COPD', 'periodontis', 'allergic rhinitis', 'esophagitis', 'epilepsy', 'sickle cell anemia', 'peripheral artery disease', 'Trichomonas Vaginalis infection']


priorDisease = [0.059, 0.29, 0.047, 0.0024, 0.002, 0.03, 0.14, 0.0765, 0.4, 0.189, 0.0033, 0.105, 0.056, 0.12, 0.044, 0.027, 0.08, 0.175, 0.0134, 0.113, 0.016, 0.017, 0.0018, 0.01, 0.000095, 0.05, 0.078, 0.0027, 0.007, 0.028, 0.03, 0.0043, 0.041, 0.195, 0.024, 0.003, 0.001, 0.003, 0.046, 0.01, 0.09, 0.11, 0.154, 0.11, 0.037, 0.2, 0.008, 0.17, 0.028, 0.02, 0.055, 0.14, 0.04, 0.16, 0.01, 0.03, 0.121, 0.091, 0.24, 0.095, 0.00019, 0.057, 0.005, 0.25, 0.000006, 0.03, 0.0000595, 0.107, 0.233, 0.0031, 0.046, 0.5, 0.11, 0.000567, 0.012, 0.00028, 0.1, 0.021]
priorSODH = [0.1, 0.036, 0.0017, 0.111, 0.118, 0.1, 0.0067, 0.076, 0.924]
D_SDH = []
SDH_D =[]

f = open("values.txt", "r")
for row in f:
	print(row)
	arr = row.split()
	for i in range(len(arr)):
		if arr[i] != "nan":
			arr[i] = float(arr[i])
	D_SDH.append(arr)

SDH_D = D_SDH


for i in range(len(SODH)):
	for j in range(len(diseases)):
 		if D_SDH[i][j] != 'nan':
 			value = D_SDH[i][j] * priorSODH[i] / priorDisease[j]
 			SDH_D[i][j] = value
 		else:
 			SDH_D[i][j] == 'nan'



print("Input the numbers of the SODH's you are interested in. Press 'q' to quit.")
for i in range(len(SODH)):
	print(str(i+1) + ". " +SODH[i])
print("")
quit = False
interest = []
while(not quit):
	num = input ("Enter number :") 
	if num == 'q':
		quit = True
	else:
 		interest.append(int(num) - 1)
print("")

probs = []
probSet = set()
diseaseDict = {}
for i in range(len(diseases)):
 	prob = priorDisease[i]
 	SDHs = ""
 	denom = 1
 	for j in range(len(interest)):
 		if(SDH_D[interest[j]][i] != "nan"):
 			prob *= SDH_D[interest[j]][i]
 			denom *= priorSODH[interest[j]]
 		if(j == 0):
 			SDHs = SDHs + SODH[interest[j]]
 		else: 
 			SDHs = SDHs + ", " + SODH[interest[j]]
 	x = prob/denom
 	probSet.add(x)
 	if x in diseaseDict.keys():
 		diseaseDict[x].append(diseases[i])
 	else:
 		diseaseDict[x] =  [diseases[i]]

for val in probSet:
	probs.append(val)


probs.sort(reverse=True)
for i in range(5):
	for j in range(len(diseaseDict[probs[i]])):
		print("P(" + diseaseDict[probs[i]][j] + " | " + SDHs + ") = " + str(probs[i]) + ".")
		print("The prior P("+diseaseDict[probs[i]][j]+") is " + str(priorDisease[diseases.index(diseaseDict[probs[i]][j])]))
		print("")




