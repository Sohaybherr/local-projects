<link rel="stylesheet" href="main.css">
<?php
include("filiereData.php");
include("etudiantData.php");

// Get the selected filiere code from the query string.
// This matches the link in main.php: listEtudiant.php?filiere=<code>
$filiere = isset($_GET['filiere']) ? $_GET['filiere'] : null;

// Validate the selection and provide a friendly message if missing.
if (!$filiere || !isset($filieres[$filiere])) {
    echo "<p style='color:red;'>Aucune filière sélectionnée ou filière invalide. <a href='main.php'>Retour à la liste des filières</a>.</p>";
    return;
}
?>

<h2>Liste des étudiants de la filière : <?php echo htmlspecialchars($filieres[$filiere]); ?></h2>

<table border="1">
<tr>
<th>Nom</th>
<th>Prénom</th>
<th>Note</th>
<th>Mention</th>
</tr>

<?php
foreach($etudiants as $e){
    if($e['filiere']==$filiere){
        echo "<tr>";
        echo "<td><a href='etudiantDetails.php?code=".$e['code']."'>".$e['nom']."</a></td>";
        echo "<td>".$e['prenom']."</td>";
        echo "<td>".$e['note']."</td>";
        echo "<td>".$e['mention']."</td>";
        echo "</tr>";
    }
}
?>
<tr>
<td colspan="4"><a href="ajouterEtudiant.php">Ajouter un étudiant</a></td>

</tr>

</table>

<br>

