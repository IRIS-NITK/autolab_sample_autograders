all:
	mkdir autograder_files
	cp soln.py autograder_files
	cp evaluation_script.py autograder_files/
	cp input-*.txt autograder_files/
	tar cvf autograde.tar autograder_files/
	echo "autograde-Makefile and autograde.tar are ready for upload"
	rm -rf autograder_files
clean:
	rm -f input-*.txt soln.py
	rm -f autograde.tar
	rm -rf autograder_files/
	cp .autograde-Makefile autograde-Makefile
	cp .evaluation_script.py evaluation_script.py
	touch input-0.txt input-1.txt input-2.txt soln.py
	clear && cat README.txt
