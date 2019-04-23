import os
import os.path
import functions as lib
	

truth_list = os.listdir('truth.txt')
for truth_name in truth_list:
	f = open(lib.TRUTH_FOLDER+truth_name, "r") #open truth_ground file for actor in n-th time performed all actions.
	person_name = truth_name[:-10]
	print person_name
	truth_talble = []
	#read content of file txt
	for line in f.readlines():
		truth_talble.append(int(line))
	# print(truth_talble)
	truth_talble_array = lib.read_txt(truth_talble)
	#check exist
	if os.path.exists("histograms") == False:
		os.mkdir("histograms")
	if os.path.exists("histograms/"+person_name) == False:
		os.mkdir("histograms/"+person_name)
	#5 cams record 5 views, loops through each cam
	for i in range(0,5):
		if os.path.exists("histograms/"+person_name+"/"+str(i)) == False:
			os.mkdir("histograms/"+person_name+"/"+str(i))

		cam_dir = lib.IXMAS_FOLDER+person_name+".pictures/"+person_name+"_png/"+"cam"+str(i)#i-th cam of person_name
		# frame_list = os.listdir(folder_name) #list of frames for each cam
		lib.cal_histogram(truth_talble_array, person_name, cam_dir)
		print("Finish calculating histos for {} cam: {}".format(person_name, i))
		#print(frame_list)
	f.close()
