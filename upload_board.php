<?php

header('Access-Control-Allow-Origin: *');

$conn = mysqli_connect('', '', '', '');

if (isset($_GET['var'])) {
   $var = explode(',', $_GET['var']);
   $id  = 0;
   $sql    = 'SELECT * FROM custom WHERE board =\'' . mysqli_escape_string($conn, $var[0]) . '\' AND difficulty = \'' . mysqli_escape_string($conn, $var[1]) . '\'';
   $result = mysqli_query($conn, $sql);
   $count  = mysqli_num_rows($result);
   if ($count >= 1) {
      $row = mysqli_fetch_assoc($result);
      $id  = $row['id'];
   } else {
      $sql    = 'SELECT * FROM custom';
      $result = mysqli_query($conn, $sql);
      $count  = mysqli_num_rows($result);
      $id = $count + 1;
      $t  = time();
      if ($count >= 1000) {
         $sql    = 'SELECT id, generated FROM custom ORDER BY generated ASC LIMIT 1';
         $result = mysqli_query($conn, $sql);
         $row    = mysqli_fetch_assoc($result);
         $id     = $row['id'];
         $sql = 'UPDATE custom SET board=\'' . mysqli_escape_string($conn, $var[0]) . '\', difficulty = \'' . mysqli_escape_string($conn, $var[1]) . '\', generated = \'' . mysqli_escape_string($conn, $t) . '\' WHERE id = ' . mysqli_escape_string($conn, $id);
         mysqli_query($conn, $sql);
      } else {
         $sql = 'INSERT INTO custom(id, board, difficulty, generated) VALUES (' . mysqli_escape_string($conn, $id) . ', \'' . mysqli_escape_string($conn, $var[0]) . '\', \'' . mysqli_escape_string($conn, $var[1]) . '\', \'' . mysqli_escape_string($conn, $t) . '\')';
        
         mysqli_query($conn, $sql);
      }
   }
   echo ($id);
}

?>