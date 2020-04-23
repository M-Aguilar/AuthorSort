This simple program takes a .txt file containing a list of full author names.
It removes punctuation and produces a consistent naming convention.

For example:
John H. Smith 		--> 	Smith, J. H.
Yukon Gold 		--> 	Gold, Y.
Martin Van Buren 	--> 	Van Buren, M.

The user is prompted to provide the number of initial key authors that ignore the alphabetical surname order.

The exceptions 'van', 'de', 'el', 'al', 'ibn', and 'abd' are decided on a case by case basis. 
If any exceptions are found in a Author Name, the user is prompted to type the full name as to be displayed. 
The exceptions variable is available at line 4 of the .py file. Adjust your exceptions as necessary. 

Names consisting of three or more names in which the last name is not consistent with the current character index will prompt the user to select the last name.
