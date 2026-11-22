<?php
include("auth.php");
include("header.php");
include("data.php");

$codeFiliere = isset($_GET["code"]) ? $_GET["code"] : "";
$intitule = getIntituleFiliere($codeFiliere, $filieres);
?>

<h3>Liste des étudiants réussis - <?php echo $intitule; ?></h3>

<table>
    <tr>
        <th>Code</th>
        <th>Nom</th>
        <th>Prénom</th>
        <th>Note</th>
    </tr>

    <?php
    foreach ($etudiants as $etudiant) {
        if ($etudiant["Filiere"] == $codeFiliere && $etudiant["Note"] >= 10) {
            echo "<tr>";
            echo "<td><a href='DetailsEtudiant.php?code=" . $etudiant["CodeEtudiant"] . "'>" . $etudiant["CodeEtudiant"] . "</a></td>";
            echo "<td><a href='DetailsEtudiant.php?code=" . $etudiant["CodeEtudiant"] . "'>" . $etudiant["Nom"] . "</a></td>";
            echo "<td><a href='DetailsEtudiant.php?code=" . $etudiant["CodeEtudiant"] . "'>" . $etudiant["Prenom"] . "</a></td>";
            echo "<td>" . $etudiant["Note"] . "</td>";
            echo "</tr>";
        }
    }
    ?>
</table>

<p>
    <a href="AjouterEtudiant.php">Ajouter un nouvel étudiant</a>
</p>

<?php include("footer.php"); ?>