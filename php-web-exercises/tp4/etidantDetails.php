<link rel="stylesheet" href="main.css">
<?php
include("data.php");
include("filiereDa");

$code = $_GET['code'];

foreach($etudiants as $e){
    if($e['code']==$code){
        $etudiant = $e;
    }
}
?>

<h2>Détail de l'étudiant : <?php echo $etudiant['code']; ?></h2>

<p>Nom : <?php echo $etudiant['nom']; ?></p>
<p>Prénom : <?php echo $etudiant['prenom']; ?></p>
<p>Note : <?php echo $etudiant['note']; ?></p>
<p>Filière : <?php echo $etudiant['filiere']; ?></p>

<a href="modifier.php?code=<?php echo $etudiant['code']; ?>">Modifier</a>
<a href="supprimer.php?code=<?php echo $etudiant['code']; ?>">Supprimer</a>