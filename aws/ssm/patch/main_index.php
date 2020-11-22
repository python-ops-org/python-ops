<?php

extract($_POST);

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://lmhssl9tsb.execute-api.us-east-1.amazonaws.com/dev",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\n  \"r\": \"$region\",\n  \"i\": \"$instance\",\n  \"c\": \"$cmd\"\n}",
  CURLOPT_HTTPHEADER => array(
    "cache-control: no-cache",
    "content-type: application/json",
    "postman-token: 9e326fca-945c-347f-6e21-c38a00cd4e12"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
