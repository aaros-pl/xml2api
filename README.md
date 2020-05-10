Creates XML from given JSON for http POST request, library used: json2xml

Sample http request via curl:
curl -d json='{"login":"aaros","id":1,"your_value":"some_http_string_or_somethin_else"}' -X POST http://localhost:1234/api

Response:
<?xml version="1.0" ?>
<all>
        <login type="str">aaros</login>
        <id type="int">1</id>
        <your_value type="str">some_http_string_or_somethin_else</your_value>
</all>
