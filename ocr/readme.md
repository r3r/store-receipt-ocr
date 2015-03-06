#Basic Store Receipt OCR

##Overview
Basic Store Receipt OCR exposed via a REST API.

##Architecture
Uses the following libraries:
* pytesser - A Tesseract wrapper for python
* Flask RESTFull(and by extension Flask) - for REST API

All non-standard Python2.7 libraries are included.

##Usage
* Execute the endpoint.py file.
* Call the url http://<ServerIP>:5000 using HTTP POST.
* The call requires one POST parameter: image64 . This should contain the base64 encoded image file.
    * base64 encode can be a maximum of 25KB.
* If successful returns a JSON object with two keys: 'raw' and 'structure'
    * 'raw' - contains the raw OCR string
    * 'structure' - contains a dictionary of item-price values
* On ubuntu(linux) install tesseract-ocr and python-imaging
    * `apt-get install python-imaging tesseract-ocr`
