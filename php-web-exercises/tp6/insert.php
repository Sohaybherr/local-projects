<?php
include("data.php");

$t = [
    "CodeE" => $_POST["CodeE"],
    "Nom" => $_POST["Nom"],
    "Prenom" => $_POST["Prenom"],
    "Filiere" => $_POST["Filiere"],
    "Note" => $_POST["Note"]
];

AjouterEtudiant($t);

header("Location: listeEtudiants.php?code=" . $t["Filiere"]);
exit();
?>