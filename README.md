# python-forensic-tool

This tool is a very basic python script for getting hidden strings from various file types.
It is designed for my Master's digital forensic subject to find specific and non-specific outputs for various \*nix terminal commands in relation to various files in a directory.

Haven't figured out how to get it to save output yet. 

Temporary method is:
   python3 fsv2.py |& tee output.txt

This will the output of the script the .txt file
 
In the future I'll try to expand on this project by:
  - adding automatic decoding for various encoding types found in the files e.g. base64, md5, sha1.
  - handling images as images to potentially pull text from them or scan QRcodes/barcodes.
