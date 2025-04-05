<?php
$choices = implode(',', $_GET['choices']);

$command = escapeshellcmd("python3 party_planner.py --choices $choices");

$output = shell_exec($command);
echo $output;
?>