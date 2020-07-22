<?php

header('Access-Control-Allow-Origin: *');

$conn = mysqli_connect('', '', '', '');

if (isset($_GET['id'])) {
   $sql = 'SELECT * FROM custom WHERE id =' . mysqli_escape_string($conn, $_GET['id']);
   $result = mysqli_query($conn, $sql);
   $row    = mysqli_fetch_assoc($result);
   echo ($row['board']);
   echo ($row['difficulty']);
}
?>