<?php

header('Access-Control-Allow-Origin: *');

$conn = mysqli_connect('', '', '', '');

if (isset($_GET['var'])) {
   $var = explode(",", $_GET["var"]);
   $sql = "SELECT * FROM " . mysqli_escape_string($conn, $var[0]) . " WHERE id = " . mysqli_escape_string($conn, $var[1]);
   $result = mysqli_query($conn, $sql);
   $row = mysqli_fetch_assoc($result);
   echo ($row['board']);
}

?>