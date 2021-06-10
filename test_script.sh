#!/usr/bin/env bash



   main () {
	
	echo "" > test/test_results.txt
	
   	cat test/inputs_enc.txt | python3 main.py -e test/file1.txt > /dev/null
	cat test/inputs_dec.txt | python3 main.py -d test/new_enc.txt > /dev/null
	
	if cmp test/file1.txt test/new_enc.txt; then
		echo "Encrypted then decrypted test/file1.txt matches the expected result." >> test/test_results.txt
		echo "Encrypted then decrypted test/file1.txt matches the expected result."

   	else
   		echo "ERROR: Encrypted then decrypted test/file1.txt does NOT matches the expected result." >> test/test_results.txt
		echo "ERROR: Encrypted then decrypted test/file1.txtt does NOT matches the expected result." 
                exit 1

	fi
	
	cat test/inputs_enc.txt | python3 main.py -e test/example.txt > /dev/null
	cat test/inputs_dec.txt | python3 main.py -d test/new_enc.txt > /dev/null

	if cmp test/example.txt test/new_enc.txt; then
		echo "Encrypted then decrypted test/example.txt matches the expected result." >> test/test_results.txt
		echo "Encrypted then decrypted test/example.txt matches the expected result."

   	else
   		echo "ERROR: Encrypted then decrypted test/example.txt does NOT matches the expected result." >> test/test_results.txt
		echo "ERROR: Encrypted then decrypted test/example.txt does NOT matches the expected result."
                exit 1

	fi

	
	exit 0
}


main "$@"
