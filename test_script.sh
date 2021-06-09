#!/usr/bin/env bash



   main () {

   	cat test/inputs_enc.txt | python3 main.py -e test/file1.txt

	if cmp test/enc_results.txt test/new.txt; then
		echo "Encrypted file matches the expected result." >> test/test_results.txt

   	else
   		echo "ERROR: Encrypted file does NOT matches the expected result." > test/test_results.txt
                exit 1

	fi
	exit 0
}


main "$@"
