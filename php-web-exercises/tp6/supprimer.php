<?php
include("data.php");

$code = isset($_GET["code"]) ? $_GET["code"] : "";
$filiere = isset($_GET["filiere"]) ? $_GET["filiere"] : "";

if ($code != "") {
    SupprimerEtudiant($code);
}

header("Location: listeEtudiants.php?code=" . $filiere);
exit();
?>