<?php
$text = $_GET['text'];
$file = fopen("clip.txt", "w");
fwrite($file, $text);
fclose($file);

