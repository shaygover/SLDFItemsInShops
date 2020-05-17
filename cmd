sort itemCollection_SLDF_Mech_light_lvl-0.csv | cut -d , -f 1,2,3 | uniq 
sed -e 's/$/,1/' -i itemCollection_SLDF_Mech_light_lvl-0.csv
