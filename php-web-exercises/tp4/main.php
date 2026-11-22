<?php
include("filiereData.php");
?>

<h2>Liste des filières</h2>

<ul>
<?php
foreach($filieres as $code => $nom){
    echo "<li><a href='listEtudiant.php?filiere=$code'>$nom</a></li>";
}
?>
</ul>