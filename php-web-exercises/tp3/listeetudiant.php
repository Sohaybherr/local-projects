<?php include("header.php"); ?>

<?php
$code = isset($_GET["code"]) ? $_GET["code"] : "";

$etudiants = [
    ["Nom" => "Alaoui",   "Prenom" => "Ahmed",  "Filiere" => "GI",  "Note" => 15],
    ["Nom" => "Bennani",  "Prenom" => "Salma",  "Filiere" => "GI",  "Note" => 8],
    ["Nom" => "Karimi",   "Prenom" => "Youssef","Filiere" => "SMI", "Note" => 14],
    ["Nom" => "Tazi",     "Prenom" => "Imane",  "Filiere" => "SMI", "Note" => 17],
    ["Nom" => "Lahlou",   "Prenom" => "Omar",   "Filiere" => "SMA", "Note" => 9],
    ["Nom" => "Idrissi",  "Prenom" => "Meryem", "Filiere" => "SMA", "Note" => 13],
    ["Nom" => "Hakimi",   "Prenom" => "Anas",   "Filiere" => "SMP", "Note" => 11],
    ["Nom" => "Amrani",   "Prenom" => "Sara",   "Filiere" => "SVI", "Note" => 16]
];
?>

<h2>Liste des étudiants réussis</h2>
<p>Filière : <?php echo $code; ?></p>

<table border="1" cellpadding="8" cellspacing="0">
    <tr>
        <th>Nom</th>
        <th>Prénom</th>
        <th>Filière</th>
        <th>Note</th>
    </tr>

    <?php
    foreach ($etudiants as $etudiant) {
        if ($etudiant["Filiere"] == $code && $etudiant["Note"] >= 10) {
            echo "<tr>";
            echo "<td>" . $etudiant["Nom"] . "</td>";
            echo "<td>" . $etudiant["Prenom"] . "</td>";
            echo "<td>" . $etudiant["Filiere"] . "</td>";
            echo "<td>" . $etudiant["Note"] . "</td>";
            echo "</tr>";
        }
    }
    ?>
</table>

<br>
<a href="ListeFilieres.php">Retour à la liste des filières</a>

<?php include("footer.php"); ?>