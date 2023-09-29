for temp in 100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 
do
for press in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
	do
		echo $temp $press
		folder="${temp}K_${press}atm"
		cp -r BASE $folder
	        cd $folder
		sed -i "s/TEMPERATURE/$temp/g" start.lmp 
		sed -i "s/TEMPERATURE/$temp/g" job.sh
		sed -i "s/PRESSURE/$press/g" start.lmp 
		sed -i "s/PRESSURE/$press/g" job.sh
		sbatch < job.sh
		cd ..	
	done
done
