#!/usr/bin/env bash



   main () {

   	cat test/inputs_enc.txt | python3 -m main.py -e testfile1.txt

 
}


main "$@"
