#!/usr/bin/env bash



   main () {
	
	echo "" > test/test_results.txt
	
   	cat test/inputs_enc.txt | python3 main.py -e test/file1.txt

	if cmp test/enc_results.txt test/new_enc.txt; then
		echo "Encrypted file matches the expected result." >> test/test_results.txt
		echo "Encrypted file matches the expected result."

   	else
   		echo "ERROR: Encrypted file does NOT matches the expected result." >> test/test_results.txt
		echo "ERROR: Encrypted file does NOT matches the expected result."
                exit 1

	fi
	
	cat test/inputs_dec.txt | python3 main.py -d test/new_enc.txt
	
	if cmp test/file1.txt test/new_enc.txt; then
		echo "derypted file matches the expected result." >> test/test_results.txt
		echo "derypted file matches the expected result."

   	else
   		echo "ERROR: derypted file does NOT matches the expected result." >> test/test_results.txt
		echo "ERROR: derypted file does NOT matches the expected result." 
                exit 1

	fi
	
	exit 0
}


main "$@"
