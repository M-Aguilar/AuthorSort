This simple program takes a txt file containing a list of full author names.
It removes punctuation and produces a consistent naming convention.

For example:
John H. Smith --> Smith, J. H.
Yukon Gold --> Gold, Y.
Martin Van Buren --> Van Buren, M.

The user is initially prompted ot input the number of key authors in order to avoid prompting for the proper last name as it part of the process 
when processing the chronological names throughout the remainder of the list.
The exceptions 'van', 'de', 'el', 'al', 'ibn', and 'abd' are decided on a case by case basis. 
The user is prompted to type the name as desired to be displayed. 
Names consisting of 3 or more names in which the last name is not consistend with the current character index  will also prompt the user to select the proper last name.


