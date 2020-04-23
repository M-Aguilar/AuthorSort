#Author Moises Aguilar
import string

exceptions = ['van', 'de', 'el','al','ibn','abd']

def ex_help():
	ex_list = []
	for ex in exceptions:
		ex_list.append(' ' + ex + ' ')
	return ex_list

def prompt(name):
	for i in name:
		print(str(name.index(i)) + ' : ' + i)
	ui = input("Please enter the number representing the correct last name: ")
	while (not ui.isdigit() or int(ui) > len(name) - 1):
		ui = input("please enter a valid number: 0 through " + str(len(name) - 1) + ': ')
	nn = ''
	for i in name[int(ui):]:
		nn += i
	return nn.capitalize()

def authors():
	ui = input("how many key authors are there? Enter a number: ")
	while(not ui.isdigit()):
		ui = input("please enter a valid number: ")
	return int(ui)

def p_format(n_list, ka):
	cur_c = 'A'
	list_b = []
	for i in n_list:
		if len(list_b) > 0 and len(list_b) > ka and list_b[len(list_b)-1][0] is not cur_c:
			cur_c = chr(ord(list_b[len(list_b)-1][0]))#chr(ord(cur_c) + 1)
			print(cur_c)
		if any (ex in i for ex in ex_help()):
			ui = input('there is an exception in ' + i + '\n' + 'Please enter how you would like the name printed: ')
			list_b.append(ui)
		else: 
			i = i.split(' ')
			last_name = i[len(i)-1].capitalize()
			if '-' in last_name:
				last_name = last_name[0:last_name.index('-')+1]+last_name[last_name.index('-')+1:len(last_name)].capitalize()
			elif (len(list_b) > ka) and last_name[0] is not cur_c and last_name[0] is not chr(ord(cur_c) + 1):
				print("Is " + last_name + " the correct last name in " + str(i) + "?")
				print("Previous name was: " + str(list_b[len(list_b)-1]))
				last_name = prompt(i)
			initials = ''
			for n in i[0:len(i)-1]:
				if len(n) > 1:
					if '-' in n:
						initials += n[0].capitalize()+'-'+n[n.index('-')+1].capitalize() + '.'
					else:
						initials += n[0].capitalize() + '.'
				elif len(n) == 1:
					initials += n.capitalize() + '.'
			list_b.append(last_name + ', ' + initials)	
	return list_b

def clean(filename):
	new_list = []
	with open(filename, encoding="utf-8") as f:
		names = [x.strip() for x in str(f.readlines()).split(',')]
		for i in names:
			i = ''.join([j for j in i if not j.isdigit()])
			if '-' in i:
				new_list.append(i)	
			elif len(i) > 2:
				new_list.append(i.translate(str.maketrans('', '', string.punctuation)))
		return new_list
main():
	p = p_format(clean(input('Please enter the input file name.')), authors())
	new_f = input("what would you like the output file to be called?: ")
	with open(new_f, 'w', encoding="utf-8") as f_o:
		for i in p:
			if p.index(i) == len(p) - 1:
				f_o.write('and ' + i)
			else:
				f_o.write(i + ', ')

if __name__ == '__main__':
	main()
